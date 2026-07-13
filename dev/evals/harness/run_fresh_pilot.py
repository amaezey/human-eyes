#!/usr/bin/env python3
"""Run the independently sourced, ten-pair fresh benchmark pilot.

The manifest is deliberately data-oriented: each pair has ``human`` and ``ai``
document records, and every document record carries its path, sha256,
provenance, contamination declaration, and full semantic audit.  Invalid pairs
are reported but never included in the headline estimate.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import random
import re
import statistics
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_MANIFEST = ROOT / "dev/evals/samples/fresh-pilot-01/manifest.json"
DEFAULT_REPORT = ROOT / "dev/evals/fresh-pilot-report.json"
EXPECTED_PAIRS = 10
BOOTSTRAP_SEED = 20260712
BOOTSTRAP_DRAWS = 10_000
EXCLUDED_CHECKS = {"no-curly-quotes", "overall-signal-stacking"}
EVIDENCE_TYPES = {"lexical", "statistical", "aggregate"}
PAIR_METADATA_FIELDS = {
    "genre", "subgenre", "register", "era", "publication_year", "source_type",
    "intended_audience", "formatting_profile", "selection_rationale",
    "excerpt_coherence_review", "boilerplate_review", "confounds", "license", "contamination",
    "source_domain", "prose_class",
    "match_review_packet",
}


def load_grade():
    path = ROOT / "human-eyes/scripts/grade.py"
    spec = importlib.util.spec_from_file_location("grade_fresh_pilot", path)
    module = importlib.util.module_from_spec(spec)
    if spec.loader is None:
        raise RuntimeError(f"Could not load {path}")
    spec.loader.exec_module(module)
    return module


def resolve_path(value: str, manifest_path: Path) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    candidates = (manifest_path.parent / path, ROOT / path, ROOT / "dev" / path)
    return next((candidate for candidate in candidates if candidate.exists()), candidates[0])


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def packet_error(packet, manifest_path: Path, label: str) -> str | None:
    if not isinstance(packet, dict) or not packet.get("path") or not packet.get("sha256"):
        return f"{label} requires path+sha256 binding"
    path = resolve_path(packet["path"], manifest_path)
    if not path.is_file() or sha256(path) != packet["sha256"]:
        return f"{label} path/hash binding mismatch"
    return None


def _answers_error(answers, registry_ids, text, label):
    if not isinstance(answers, list):
        return f"{label} answers are not a list"
    ids = [answer.get("id") for answer in answers if isinstance(answer, dict)]
    if len(ids) != len(set(ids)) or set(ids) != set(registry_ids):
        return f"{label} IDs do not exactly match the registry"
    if any(not isinstance(answer.get("flagged"), bool) for answer in answers):
        return f"{label} flagged values must be boolean"
    for answer in answers:
        evidence = answer.get("evidence", [])
        evidence = [evidence] if isinstance(evidence, str) and evidence else (evidence or [])
        if not isinstance(evidence, list) or any(not isinstance(item, str) for item in evidence):
            return f"{label} {answer.get('id')} evidence must be text/list"
        if answer["flagged"] and (not evidence or any(item not in text for item in evidence)):
            return f"{label} {answer.get('id')} flagged evidence is absent from document"
        if not answer["flagged"] and evidence:
            return f"{label} {answer.get('id')} clear answer contains evidence"
    return None


def semantic_error(audit, registry_ids, text: str, document_hash: str, registry_hash: str) -> str | None:
    if not isinstance(audit, dict):
        return "missing semantic audit"
    if audit.get("coverage_mode") != "full" or audit.get("audit_status") != "complete":
        return "semantic audit is not complete/full"
    annotations = audit.get("annotations")
    if not isinstance(annotations, list) or len(annotations) != 2:
        return "semantic audit requires exactly two annotations"
    annotators = [item.get("annotator_id") for item in annotations if isinstance(item, dict)]
    if len(set(annotators)) != 2 or any(not value for value in annotators):
        return "semantic annotator IDs must be distinct"
    annotation_ids = []
    for annotation in annotations:
        if annotation.get("blinded") is not True or not annotation.get("randomized_sample_id"):
            return "semantic annotations must be blinded with randomized sample_id"
        if annotation.get("document_sha256") != document_hash or annotation.get("registry_sha256") != registry_hash:
            return "semantic annotation hash binding mismatch"
        if not annotation.get("annotation_id"):
            return "semantic annotation missing annotation_id"
        annotation_ids.append(annotation["annotation_id"])
        error = _answers_error(annotation.get("answers"), registry_ids, text, "semantic annotation")
        if error:
            return error
    adjudication = audit.get("adjudication")
    if not isinstance(adjudication, dict):
        return "semantic audit missing adjudication"
    if set(adjudication.get("input_annotation_ids", [])) != set(annotation_ids):
        return "semantic adjudication is not bound to both annotations"
    error = _answers_error(adjudication.get("final_answers"), registry_ids, text, "semantic adjudication")
    if error:
        return error
    agreement = adjudication.get("agreement_summary")
    if not isinstance(agreement, dict) or set(agreement) != set(registry_ids) or any(not isinstance(value, bool) for value in agreement.values()):
        return "semantic adjudication requires per-check agreement summary"
    return None


def provenance_error(record, cohort: str) -> str | None:
    provenance = record.get("provenance")
    if not isinstance(provenance, dict):
        return "missing provenance"
    if cohort == "human":
        required = ("source_url", "title", "author")
    else:
        required = ("model", "provider", "generated_at", "first_output_path", "first_output_sha256",
                    "parameters", "blind_generation", "attempt_number", "selection_rule")
    missing = [key for key in required if key not in provenance or provenance.get(key) in ("", {})]
    if cohort == "ai" and not (provenance.get("prompt_text") or
                               (provenance.get("prompt_path") and provenance.get("prompt_sha256"))):
        missing.append("prompt_text or prompt_path+prompt_sha256")
    if cohort == "ai" and not isinstance(provenance.get("parameters"), dict):
        missing.append("parameters object (explicit null allowed per setting)")
    elif cohort == "ai":
        absent_settings = {"temperature", "top_p", "max_output_tokens", "seed"} - set(provenance["parameters"])
        if absent_settings:
            missing.append("parameters missing " + ", ".join(sorted(absent_settings)))
    if cohort == "ai" and provenance.get("blind_generation") is not True:
        missing.append("blind_generation=true")
    return f"provenance missing {', '.join(missing)}" if missing else None


def contamination_error(record) -> str | None:
    declaration = record.get("contamination")
    if not isinstance(declaration, dict):
        return "missing contamination declaration"
    if not isinstance(declaration.get("checked"), bool) or not declaration.get("method"):
        return "contamination declaration requires checked boolean and method"
    if declaration["checked"] is not True:
        return "contamination check was not completed"
    if "known_overlap" not in declaration:
        return "contamination declaration requires known_overlap"
    if declaration.get("known_overlap") not in (False, []):
        return "known corpus contamination declared"
    return None


def grade_document(grade, path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    # Compare prose, not transport markup.  A whitespace count treats each URL
    # as one word, while punctuation-tokenisers can turn a long URL into many
    # fake words.  Strip link targets and count alphabetic word tokens so the
    # length gate measures readable content consistently across web extracts,
    # email, and generated plain text.
    prose = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    prose = re.sub(r"https?://\S+", " ", prose)
    words = len(re.findall(r"(?u)\b[^\W\d_]+(?:[’'-][^\W\d_]+)*\b", prose))
    checks = {}
    for check_id, check in grade.ALL_CHECKS.items():
        result = check(text)
        evidence_type = result.get("evidence_type")
        item = {
            "evidence_type": evidence_type,
            "candidate_count": result.get("candidate_count"),
            "threshold_met": result.get("threshold_met"),
            "context_gate": result.get("context_gate"),
            "explanation": result.get("evidence"),
            "threshold": result.get("threshold"),
        }
        if evidence_type == "lexical":
            item.update(match_count=result.get("match_count"), spans=result.get("spans"))
        elif evidence_type == "statistical":
            item.update(metric_value=result.get("metric_value"), sample_size=result.get("sample_size"))
        elif evidence_type == "aggregate":
            item.update(component_signals=result.get("component_signals"), component_count=result.get("component_count"))
        checks[check_id] = item
    surface = sum(bool(item["threshold_met"]) for key, item in checks.items() if key not in EXCLUDED_CHECKS)
    return {"path": str(path), "word_count": words, "surface_findings": surface, "checks": checks}


def typed_evidence_errors(document: dict) -> list[str]:
    errors = []
    for check_id, result in document["checks"].items():
        kind = result.get("evidence_type")
        if kind not in EVIDENCE_TYPES:
            errors.append(f"{check_id}: invalid evidence type")
        if not isinstance(result.get("candidate_count"), int) or result["candidate_count"] < 0:
            errors.append(f"{check_id}: invalid candidate count")
        if not isinstance(result.get("threshold_met"), bool):
            errors.append(f"{check_id}: threshold_met is not boolean")
        gate = result.get("context_gate")
        if not isinstance(gate, dict) or not {"applied", "raw_evidence", "suppression_reason", "effective_threshold"} <= set(gate):
            errors.append(f"{check_id}: invalid context_gate shape")
        if "threshold" not in result or "explanation" not in result:
            errors.append(f"{check_id}: missing threshold/explanation")
        if isinstance(gate, dict) and gate.get("suppression_reason") and result.get("threshold_met"):
            errors.append(f"{check_id}: impossible flagged-and-suppressed result")
        required = {"lexical": ("match_count", "spans"), "statistical": ("metric_value", "sample_size"),
                    "aggregate": ("component_signals", "component_count")}.get(kind, ())
        if any(result.get(key) is None for key in required):
            errors.append(f"{check_id}: missing typed evidence fields")
    return errors


def era_bin(year) -> str:
    year = int(year)
    if year < 1900:
        return "pre-1900"
    if year < 1950:
        return "1900-1949"
    if year < 2000:
        return "1950-1999"
    if year < 2015:
        return "2000-2014"
    return "2015-present"


def percentile(values: list[float], probability: float) -> float:
    position = (len(values) - 1) * probability
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return values[lower]
    return values[lower] + (values[upper] - values[lower]) * (position - lower)


def statistics_for(deltas: list[int]) -> dict | None:
    if not deltas:
        return None
    mean = statistics.fmean(deltas)
    deviation = statistics.stdev(deltas) if len(deltas) > 1 else 0.0
    effect = mean / deviation if deviation else None
    rng = random.Random(BOOTSTRAP_SEED)
    boot = sorted(statistics.fmean(rng.choices(deltas, k=len(deltas))) for _ in range(BOOTSTRAP_DRAWS))
    return {
        "n_pairs": len(deltas), "mean_paired_gap": round(mean, 4),
        "paired_effect_size_dz": None if effect is None else round(effect, 4),
        "effect_size_note": "undefined because paired deltas have zero variance" if effect is None else None,
        "bootstrap_95_ci": [round(percentile(boot, .025), 4), round(percentile(boot, .975), 4)],
        "bootstrap_seed": BOOTSTRAP_SEED, "bootstrap_draws": BOOTSTRAP_DRAWS,
        "ai_higher": sum(value > 0 for value in deltas), "ties": sum(value == 0 for value in deltas),
        "reversals_human_higher": sum(value < 0 for value in deltas), "pair_deltas": deltas,
    }


def correlation(xs: list[float], ys: list[float]) -> float | None:
    if len(xs) < 2 or len(xs) != len(ys):
        return None
    x_mean, y_mean = statistics.fmean(xs), statistics.fmean(ys)
    numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, ys))
    denominator = math.sqrt(
        sum((x - x_mean) ** 2 for x in xs) * sum((y - y_mean) ** 2 for y in ys)
    )
    return None if denominator == 0 else round(numerator / denominator, 4)


def per_check_diagnostics(pairs: list[dict]) -> dict:
    if not pairs:
        return {}
    diagnostics = {}
    for check_id in pairs[0]["human"]["checks"]:
        if check_id in EXCLUDED_CHECKS:
            continue
        human_flags = sum(pair["human"]["checks"][check_id]["threshold_met"] for pair in pairs)
        ai_flags = sum(pair["ai"]["checks"][check_id]["threshold_met"] for pair in pairs)
        human_density = statistics.fmean(
            pair["human"]["checks"][check_id]["candidate_count"] * 1000
            / max(pair["human"]["word_count"], 1)
            for pair in pairs
        )
        ai_density = statistics.fmean(
            pair["ai"]["checks"][check_id]["candidate_count"] * 1000
            / max(pair["ai"]["word_count"], 1)
            for pair in pairs
        )
        diagnostics[check_id] = {
            "evidence_type": pairs[0]["human"]["checks"][check_id]["evidence_type"],
            "human_flags": human_flags,
            "ai_flags": ai_flags,
            "flag_gap_ai_minus_human": ai_flags - human_flags,
            "human_candidate_density_per_1000_words": round(human_density, 3),
            "ai_candidate_density_per_1000_words": round(ai_density, 3),
            "candidate_density_gap_ai_minus_human": round(ai_density - human_density, 3),
        }
    return diagnostics


def run(manifest_path=DEFAULT_MANIFEST) -> dict:
    manifest_path = Path(manifest_path).resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    grade = load_grade()
    registry_ids = tuple(item["id"] for item in grade.registries.load_judgement()["records"])
    registry_hash = sha256(Path(grade.registries.JUDGEMENT_PATH))
    issues, warnings, pairs, seen_paths, seen_hashes = [], [], [], set(), set()
    raw_pairs = manifest.get("pairs", [])
    if len(raw_pairs) != EXPECTED_PAIRS:
        issues.append(f"manifest: expected {EXPECTED_PAIRS} pairs, found {len(raw_pairs)}")
    started = time.perf_counter()
    for index, pair in enumerate(raw_pairs, 1):
        pair_id = pair.get("id") or pair.get("slug") or f"pair-{index:02d}"
        output = {"id": pair_id, "eligible": True, "issues": []}
        metadata = pair.get("metadata", {})
        if not isinstance(metadata, dict):
            metadata = {}
        # Top-level fields are accepted for a compact, readable manifest.
        metadata = {key: pair.get(key, metadata.get(key)) for key in PAIR_METADATA_FIELDS}
        missing = sorted(key for key, value in metadata.items()
                         if key not in {"era", "publication_year"} and value in (None, ""))
        if metadata.get("era") in (None, "") and metadata.get("publication_year") in (None, ""):
            missing.append("era/publication_year")
        if metadata.get("publication_year") not in (None, ""):
            expected_era = era_bin(metadata["publication_year"])
            if int(metadata["publication_year"]) > 2019:
                output["issues"].append("metadata publication_year exceeds pre-2020 cutoff")
            if metadata.get("era") not in (None, "", expected_era):
                output["issues"].append(f"metadata era must use explicit bin {expected_era}")
            metadata["era"] = expected_era
        if missing:
            output["issues"].append(f"metadata missing {', '.join(missing)}")
        for review in ("excerpt_coherence_review", "boilerplate_review"):
            if metadata.get(review) is not True:
                output["issues"].append(f"metadata {review} must be true")
        if not isinstance(metadata.get("confounds"), list):
            output["issues"].append("metadata confounds must be a list")
        pair_contamination = contamination_error({"contamination": metadata.get("contamination")})
        if pair_contamination:
            output["issues"].append(f"metadata: {pair_contamination}")
        error = packet_error(metadata.get("match_review_packet"), manifest_path, "match_review_packet")
        if error:
            output["issues"].append(f"metadata: {error}")
        output["metadata"] = metadata
        for cohort in ("human", "ai"):
            record = pair.get(cohort)
            if not isinstance(record, dict):
                output["issues"].append(f"{cohort}: missing document record")
                continue
            for error in (provenance_error(record, cohort), contamination_error(record)):
                if error:
                    output["issues"].append(f"{cohort}: {error}")
            error = packet_error(record.get("contamination_evidence_packet"), manifest_path,
                                 "contamination_evidence_packet")
            if error:
                output["issues"].append(f"{cohort}: {error}")
            if cohort == "human":
                error = packet_error(record.get("source_packet"), manifest_path, "source_packet")
                if error:
                    output["issues"].append(f"human: {error}")
            path_value = record.get("path")
            if not path_value:
                output["issues"].append(f"{cohort}: missing path")
                continue
            path = resolve_path(path_value, manifest_path)
            if not path.is_file():
                output["issues"].append(f"{cohort}: file not found: {path_value}")
                continue
            actual_hash = sha256(path)
            if record.get("sha256") != actual_hash:
                output["issues"].append(f"{cohort}: sha256 mismatch")
            canonical = str(path.resolve())
            if canonical in seen_paths or actual_hash in seen_hashes:
                output["issues"].append(f"{cohort}: duplicate sample")
            seen_paths.add(canonical); seen_hashes.add(actual_hash)
            text = path.read_text(encoding="utf-8")
            error = semantic_error(record.get("semantic_audit"), registry_ids, text, actual_hash, registry_hash)
            if error:
                output["issues"].append(f"{cohort}: {error}")
            graded = grade_document(grade, path)
            adjudication = record.get("semantic_audit", {}).get("adjudication", {})
            answers = adjudication.get("final_answers", [])
            graded["semantic_findings"] = sum(answer.get("flagged") is True for answer in answers)
            graded["semantic_agreement"] = adjudication.get("agreement_summary")
            output[cohort] = graded
            output["issues"].extend(f"{cohort}: {error}" for error in typed_evidence_errors(graded))
            if cohort == "ai":
                provenance = record.get("provenance", {})
                for prefix in ("first_output", "prompt"):
                    value = provenance.get(f"{prefix}_path")
                    if value:
                        bound = resolve_path(value, manifest_path)
                        if not bound.is_file() or provenance.get(f"{prefix}_sha256") != sha256(bound):
                            output["issues"].append(f"ai: {prefix} path/hash binding mismatch")
        if "human" in output and "ai" in output:
            ratio = output["ai"]["word_count"] / max(output["human"]["word_count"], 1)
            if not .9 <= ratio <= 1.1:
                output["issues"].append(f"word match outside +/-10% (ratio {ratio:.3f})")
        output["eligible"] = not output["issues"]
        issues.extend(f"{pair_id}: {issue}" for issue in output["issues"])
        pairs.append(output)
    eligible = [pair for pair in pairs if pair["eligible"]]
    # Representation is an eligibility property of the cohort, rather than an
    # after-the-fact caveat. With ten pairs, no category may occupy over 40%.
    stratification = {}
    for field, minimum in (("genre", 4), ("source_type", 3), ("register", 3),
                           ("intended_audience", 3)):
        values = [str(pair["metadata"].get(field)) for pair in pairs if pair["metadata"].get(field) not in (None, "")]
        counts = {value: values.count(value) for value in sorted(set(values))}
        dominant = max(counts.values(), default=0)
        field_issues = []
        if len(counts) < minimum:
            field_issues.append(f"requires at least {minimum} strata, found {len(counts)}")
        if dominant > EXPECTED_PAIRS * .4:
            field_issues.append(f"one stratum dominates ({dominant}/{EXPECTED_PAIRS})")
        stratification[field] = {"counts": counts, "issues": field_issues}
        issues.extend(f"cohort {field}: {issue}" for issue in field_issues)
    cohort_eligible = not any(item["issues"] for item in stratification.values())
    domains = [pair["metadata"].get("source_domain") for pair in pairs]
    domain_counts = {value: domains.count(value) for value in set(domains) if value}
    if max(domain_counts.values(), default=0) > 2:
        issues.append("cohort source_domain: one domain contributes more than 2 pairs")
        cohort_eligible = False
    institutional = sum(str(pair["metadata"].get("source_type", "")).casefold() in
                        {"institution", "institutional", "agency", "federal", "government"} for pair in pairs)
    if institutional > 3:
        issues.append(f"cohort source_type: government/institution sources exceed 3 ({institutional})")
        cohort_eligible = False
    individual_authors = sum(pair.get("human", {}).get("provenance", {}).get("author_type") == "individual"
                             for pair in raw_pairs)
    if individual_authors < 7:
        issues.append(f"cohort authors: requires 7 named individuals, found {individual_authors}")
        cohort_eligible = False
    non_generic = sum(pair["metadata"].get("prose_class") not in (None, "generic_explainer_service") for pair in pairs)
    if non_generic < 4:
        issues.append(f"cohort prose: requires 4 non-generic-explainer pairs, found {non_generic}")
        cohort_eligible = False
    if not cohort_eligible:
        warnings.append("eligibility: representative-cohort gate failed")
    if len(eligible) < EXPECTED_PAIRS:
        warnings.append(f"eligibility: {len(eligible)}/{EXPECTED_PAIRS} pairs eligible")
    if len(eligible) < 10:
        warnings.append("sample size: fewer than 10 eligible pairs; treat estimates as pilot-only")
    surface_deltas = [pair["ai"]["surface_findings"] - pair["human"]["surface_findings"] for pair in eligible]
    semantic_deltas = [pair["ai"]["semantic_findings"] - pair["human"]["semantic_findings"] for pair in eligible]
    combined_deltas = [surface + semantic for surface, semantic in zip(surface_deltas, semantic_deltas)]
    documents = [pair[cohort] for pair in eligible for cohort in ("human", "ai")]
    agreement = {}
    for check_id in registry_ids:
        values = [pair[cohort]["semantic_agreement"][check_id]
                  for pair in eligible for cohort in ("human", "ai")]
        agreement[check_id] = {"agreements": sum(values), "disagreements": len(values) - sum(values)}
    return {
        "benchmark_status": "pilot_complete" if not issues and len(eligible) == EXPECTED_PAIRS and cohort_eligible else "incomplete",
        "claim_scope": "process-validation pilot only; not a generalisation, performance, or release claim",
        "manifest": str(manifest_path), "expected_pairs": EXPECTED_PAIRS,
        "eligible_pairs": len(eligible), "cohort_eligible": cohort_eligible, "issues": issues, "warnings": warnings,
        "stratification": stratification,
        "house_style_and_aggregate_excluded": sorted(EXCLUDED_CHECKS),
        "surface": statistics_for(surface_deltas), "semantic": statistics_for(semantic_deltas),
        "combined": statistics_for(combined_deltas),
        "diagnostics": {
            "per_check": per_check_diagnostics(eligible),
            "word_count_surface_findings_correlation": correlation(
                [document["word_count"] for document in documents],
                [document["surface_findings"] for document in documents],
            ),
        },
        "semantic_inter_annotator_agreement": agreement, "pairs": pairs,
        "performance": {"documents_graded": sum("human" in p for p in pairs) + sum("ai" in p for p in pairs),
                        "total_runtime_ms": round((time.perf_counter() - started) * 1000, 3)},
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()
    report = run(args.manifest)
    args.output.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in ("benchmark_status", "eligible_pairs", "surface", "warnings")}, indent=2, allow_nan=False))
    return 0 if report["benchmark_status"] == "pilot_complete" else 2


if __name__ == "__main__":
    raise SystemExit(main())
