#!/usr/bin/env python3
"""Contract tests for the fresh ten-pair pilot runner."""

import hashlib
import importlib.util
import json
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RUNNER = ROOT / "dev/evals/harness/run_fresh_pilot.py"
spec = importlib.util.spec_from_file_location("fresh_pilot", RUNNER)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)

HUMAN_OPENINGS = [
    "At dawn the ferry operator checks the river gauge before untying the first boat.",
    "The archive keeps handwritten council minutes in grey boxes beneath the reading room.",
    "A violin maker learns about timber by tapping each board and listening for its reply.",
    "When the market closes, volunteers carry unsold vegetables to the neighbourhood kitchen.",
    "The astronomer waited behind the school oval while clouds crossed the southern horizon.",
    "On winter mornings the baker judges the dough by touch instead of watching the clock.",
    "Residents planted salt-tolerant grasses where storm water had stripped soil from the bank.",
    "The curator found the exhibition's argument in a small repair visible under raking light.",
    "Before the rehearsal, dancers mark difficult passages slowly and talk through each collision.",
    "A mechanic records unusual engine sounds because customers rarely describe the same noise alike.",
]
AI_OPENINGS = [
    "River crews begin each morning by reviewing measurements, weather reports, and the day's passenger schedule.",
    "Local archives preserve civic records so researchers can trace decisions through original documents.",
    "Instrument makers select resonant timber through patient observation, testing, and accumulated practical knowledge.",
    "Community food programs redirect surplus produce after trading ends and distribute it through local kitchens.",
    "Public astronomy sessions depend on careful timing, clear skies, and an unobstructed view of the horizon.",
    "Experienced bakers assess fermentation through texture, temperature, aroma, and changes in the dough's volume.",
    "Coastal planting projects use salt-tolerant vegetation to stabilise exposed banks after damaging storm events.",
    "Conservators study repairs and surface details because these traces can reshape an exhibition's interpretation.",
    "Dance companies reduce rehearsal injuries by practising complex sequences slowly before returning to full speed.",
    "Repair technicians document unfamiliar sounds to compare customer reports with repeatable mechanical observations.",
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit(ids, path, registry_hash, suffix):
    answers = [{"id": value, "flagged": False, "evidence": []} for value in ids]
    return {"coverage_mode": "full", "audit_status": "complete",
            "annotations": [
                {"annotation_id": f"{suffix}-a", "annotator_id": "reviewer-a", "blinded": True,
                 "randomized_sample_id": f"blind-{suffix}-x", "document_sha256": digest(path),
                 "registry_sha256": registry_hash, "answers": answers},
                {"annotation_id": f"{suffix}-b", "annotator_id": "reviewer-b", "blinded": True,
                 "randomized_sample_id": f"blind-{suffix}-x", "document_sha256": digest(path),
                 "registry_sha256": registry_hash, "answers": answers},
            ],
            "adjudication": {"input_annotation_ids": [f"{suffix}-a", f"{suffix}-b"],
                             "final_answers": answers,
                             "agreement_summary": {value: True for value in ids}}}


def make_packet(root, name, payload):
    path = root / f"{name}.json"
    path.write_text(json.dumps(payload))
    return {"path": str(path), "sha256": digest(path)}


with tempfile.TemporaryDirectory() as directory:
    root = Path(directory)
    ids = [record["id"] for record in module.load_grade().registries.load_judgement()["records"]]
    registry_hash = module.sha256(Path(module.load_grade().registries.JUDGEMENT_PATH))
    pairs = []
    genres = ("science", "history", "guide", "speech", "essay")
    sources = ("agency", "archive", "university", "museum")
    registers = ("plain", "formal", "conversational")
    audiences = ("public", "specialist", "student")
    years = (1980, 1985, 1990, 1995, 2000, 2005, 2010, 2012, 2015, 2019)
    for index in range(10):
        human = root / f"human-{index}.md"
        ai = root / f"ai-{index}.md"
        # Pair lengths match; the index token also makes every sample unique.
        human_text = HUMAN_OPENINGS[index] + " The account follows one person through a specific task, preserving practical detail and uncertainty."
        ai_text = AI_OPENINGS[index] + " This account explains the process, its purpose, and the practical considerations that shape the final outcome."
        if len(human_text.split()) < len(ai_text.split()):
            human_text += " " + " ".join(["detail"] * (len(ai_text.split()) - len(human_text.split())))
        elif len(ai_text.split()) < len(human_text.split()):
            ai_text += " " + " ".join(["context"] * (len(human_text.split()) - len(ai_text.split())))
        human.write_text(human_text + "\n")
        ai.write_text(ai_text + "\n")
        contamination = {"checked": True, "method": "hash and phrase search", "known_overlap": False}
        source_packet = make_packet(root, f"source-{index}", {"licence_evidence": "public test fixture", "retrieved": True})
        human_contamination_packet = make_packet(root, f"human-contamination-{index}", {"queries": [f"human-{index}"]})
        ai_contamination_packet = make_packet(root, f"ai-contamination-{index}", {"queries": [f"ai-{index}"]})
        match_packet = make_packet(root, f"match-{index}", {"human_words": len(human_text.split()), "ai_words": len(ai_text.split())})
        pairs.append({
            "id": f"pair-{index}",
            "metadata": {
                "genre": genres[index % len(genres)], "subgenre": f"kind-{index}",
                "register": registers[index % len(registers)], "publication_year": years[index],
                "source_type": sources[index % len(sources)],
                "intended_audience": audiences[index % len(audiences)],
                "formatting_profile": "plain paragraphs", "selection_rationale": "tests a declared stratum",
                "excerpt_coherence_review": True, "boilerplate_review": True,
                "confounds": [], "license": "test fixture",
                "contamination": {"checked": True, "method": "cohort review", "known_overlap": False},
                "source_domain": f"source-{index // 2}.test",
                "prose_class": "generic_explainer_service" if index < 4 else "essay_or_narrative",
                "match_review_packet": match_packet,
            },
            "human": {"contamination": contamination, "contamination_evidence_packet": human_contamination_packet,
                      "source_packet": source_packet, "semantic_audit": audit(ids, human, registry_hash, f"human-{index}"),
                      "path": str(human), "sha256": digest(human),
                      "provenance": {"source_url": f"https://example.test/{index}", "source_domain": f"source-{index // 2}.test",
                                     "title": f"Title {index}", "author": f"Author {index}", "author_type": "individual"}},
            "ai": {"contamination": contamination, "contamination_evidence_packet": ai_contamination_packet,
                   "semantic_audit": audit(ids, ai, registry_hash, f"ai-{index}"),
                   "path": str(ai), "sha256": digest(ai),
                   "provenance": {"model": "test-model", "provider": "test-provider",
                                  "generated_at": "2026-07-12T00:00:00Z", "prompt_text": f"Write sample {index}",
                                  "first_output_path": str(ai), "first_output_sha256": digest(ai),
                                  "parameters": {"temperature": None, "top_p": None,
                                                 "max_output_tokens": None, "seed": None},
                                  "blind_generation": True,
                                  "attempt_number": 1, "selection_rule": "first output only"}},
        })
    manifest = root / "manifest.json"
    manifest.write_text(json.dumps({"pairs": pairs}))
    report = module.run(manifest)
    assert report["benchmark_status"] == "pilot_complete", report["issues"]
    assert report["eligible_pairs"] == 10
    assert report["performance"]["documents_graded"] == 20
    assert not report["warnings"]
    assert report["surface"]["n_pairs"] == 10
    assert report["semantic"]["n_pairs"] == 10 and report["combined"]["n_pairs"] == 10
    assert report["diagnostics"]["per_check"]
    assert "word_count_surface_findings_correlation" in report["diagnostics"]
    assert all(
        "flag_gap_ai_minus_human" in item and "candidate_density_gap_ai_minus_human" in item
        for item in report["diagnostics"]["per_check"].values()
    )
    assert set(report["semantic_inter_annotator_agreement"]) == set(ids)
    assert report["surface"]["bootstrap_seed"] == module.BOOTSTRAP_SEED
    assert len(report["surface"]["bootstrap_95_ci"]) == 2
    assert report["surface"]["ai_higher"] + report["surface"]["ties"] + report["surface"]["reversals_human_higher"] == 10
    assert all(not value["issues"] for value in report["stratification"].values())
    for pair in report["pairs"]:
        for cohort in ("human", "ai"):
            for result in pair[cohort]["checks"].values():
                assert result["evidence_type"] in module.EVIDENCE_TYPES
                assert isinstance(result["candidate_count"], int) and result["candidate_count"] >= 0

    compact_pairs = json.loads(json.dumps(pairs))
    for pair in compact_pairs:
        pair.update(pair.pop("metadata"))
    compact_manifest = root / "compact-manifest.json"
    compact_manifest.write_text(json.dumps({"pairs": compact_pairs}))
    compact_report = module.run(compact_manifest)
    assert compact_report["benchmark_status"] == "pilot_complete", compact_report["issues"]

    # A hash failure, incomplete semantic audit, word mismatch, and dominant
    # cohort must be visible and must prevent a misleading complete result.
    broken = json.loads(manifest.read_text())
    broken["pairs"][0]["human"]["sha256"] = "0" * 64
    broken["pairs"][1]["ai"]["semantic_audit"]["audit_status"] = "pending"
    broken["pairs"][2]["ai"]["path"] = broken["pairs"][0]["ai"]["path"]
    broken["pairs"][2]["ai"]["sha256"] = broken["pairs"][0]["ai"]["sha256"]
    for pair in broken["pairs"]:
        pair["metadata"]["genre"] = "one-genre"
        pair["metadata"]["source_domain"] = "dominant.gov"
        pair["metadata"]["source_type"] = "government"
        pair["metadata"]["prose_class"] = "generic_explainer_service"
        pair["human"]["provenance"]["author_type"] = "agency"
    broken["pairs"][3]["metadata"]["contamination"] = {"checked": True, "method": "", "known_overlap": True}
    broken["pairs"][4]["ai"]["provenance"].pop("selection_rule")
    broken["pairs"][5]["human"]["semantic_audit"]["annotations"][0]["answers"][0] = {
        "id": ids[0], "flagged": True, "evidence": ["fabricated quotation"]}
    broken["pairs"][6]["metadata"]["era"] = "recent"
    broken["pairs"][7]["metadata"]["match_review_packet"]["sha256"] = "0" * 64
    broken["pairs"][8]["human"]["semantic_audit"]["annotations"] = broken["pairs"][8]["human"]["semantic_audit"]["annotations"][:1]
    broken["pairs"][9]["ai"]["semantic_audit"].pop("adjudication")
    manifest.write_text(json.dumps(broken))
    failed = module.run(manifest)
    assert failed["benchmark_status"] == "incomplete"
    assert failed["eligible_pairs"] < 10
    assert any("sha256 mismatch" in issue for issue in failed["issues"])
    assert any("semantic audit is not complete" in issue for issue in failed["issues"])
    assert any("duplicate sample" in issue for issue in failed["issues"])
    assert failed["stratification"]["genre"]["issues"]
    assert any("eligibility" in warning for warning in failed["warnings"])
    for phrase in ("source_domain", "government/institution", "named individuals", "non-generic-explainer",
                   "contamination declaration", "selection_rule", "flagged evidence is absent", "explicit bin"):
        assert any(phrase in issue for issue in failed["issues"]), phrase
    assert any("path/hash binding mismatch" in issue for issue in failed["issues"])
    assert any("exactly two annotations" in issue for issue in failed["issues"])
    assert any("missing adjudication" in issue for issue in failed["issues"])

    # Exercise the two other annotation-integrity failures independently.
    one_audit = audit(ids, human, registry_hash, "red")
    one_audit["annotations"][1]["annotator_id"] = "reviewer-a"
    assert "distinct" in module.semantic_error(one_audit, ids, human.read_text(), digest(human), registry_hash)
    one_audit = audit(ids, human, registry_hash, "red2")
    one_audit["annotations"][0]["blinded"] = False
    assert "blinded" in module.semantic_error(one_audit, ids, human.read_text(), digest(human), registry_hash)

    impossible = {"checks": {"x": {"evidence_type": "lexical", "candidate_count": 1,
        "threshold_met": True, "context_gate": {"applied": True, "raw_evidence": "x",
        "suppression_reason": "suppressed", "effective_threshold": 2}, "threshold": 2,
        "explanation": "x", "match_count": 1, "spans": []}}}
    assert any("flagged-and-suppressed" in error for error in module.typed_evidence_errors(impossible))

print("ALL PASSED: fresh pilot validity, representation, evidence, and statistics contracts")
