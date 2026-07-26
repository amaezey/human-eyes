#!/usr/bin/env python3
"""Validate one newly ingested or updated human-eyes source record."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = (
    "Metadata",
    "Summary",
    "Main insights",
    "Evidence and claims to extract",
    "Skill-use audit",
    "Matched patterns / rules",
    "Associated hypotheses",
    "Questions / follow-up",
    "Update provenance",
    "Decision history",
    "Project coverage",
    "Recommendations",
    "Evaluation of approved changes",
    "Document review",
)

REQUIRED_METADATA = (
    "URL",
    "Author / owner",
    "Published",
    "Retrieved",
    "Extracted",
    "Source type",
    "Evidence tier",
    "Review mode",
    "Stable identifier",
    "Version / revision",
    "Full-text status",
    "Snapshot",
    "Extraction method",
    "Snapshot SHA-256",
    "Model / corpus scope",
    "Access limitations",
)

REVIEW_COLUMNS = (
    "Source claim or example",
    "Evidence assessment",
    "Existing project coverage",
    "Missing or challenged",
    "Recommendation",
    "User decision",
    "Implementation status",
)

USER_DECISIONS = frozenset({"pending", "approved", "approved with changes", "rejected"})
IMPLEMENTATION_STATUSES = frozenset(
    {
        "not started",
        "in progress",
        "implemented",
        "review required",
        "blocked",
        "superseded",
        "not applicable",
    }
)
STATUS_TRANSITIONS = {
    "pending": frozenset({"not started", "review required"}),
    "approved": frozenset({"not started", "in progress", "implemented", "blocked", "not applicable"}),
    "approved with changes": frozenset(
        {"not started", "in progress", "implemented", "blocked", "not applicable"}
    ),
    "rejected": frozenset({"not applicable", "superseded"}),
}
UPDATE_PROVENANCE_COLUMNS = (
    "Version",
    "Stable identifier",
    "Snapshot",
    "Retrieved",
    "SHA-256",
)

PLACEHOLDER_RE = re.compile(
    r"<(?:[^>\n]*(?:source|author|owner|date|method|claim|finding|url|digest|model|"
    r"corpus|review|what|which|missing|existing|proposed|exact|person|organisation|"
    r"tier|route|access|material|status)[^>\n]*)>|\b(?:TBD|TODO|FIXME)\b",
    re.IGNORECASE,
)
SECTION_RE = re.compile(r"^##\s+(.+?)\s*$\n(.*?)(?=^##\s+|\Z)", re.MULTILINE | re.DOTALL)
METADATA_RE = re.compile(r"^- \*\*(.+?):\*\*\s*(.*?)\s*$", re.MULTILINE)
SHA256_RE = re.compile(r"^[0-9a-f]{64}$", re.IGNORECASE)
CLAIM_ID_RE = re.compile(r"^(C\d{2,}):\s+", re.IGNORECASE)
ANY_CLAIM_ID_RE = re.compile(r"\bC\d{2,}\b", re.IGNORECASE)
PASSED_EVALUATION_RE = re.compile(
    r"^- (C\d{2,}): passed - (\S.*\S|\S)\s*$", re.MULTILINE
)
CONFLICT_MARKERS = (b"<<<<<<< ", b"=======", b">>>>>>> ")
REVIEW_METHOD_PREFIXES = (
    "independent source-record reviewer:",
    "self-review fallback: subagents unavailable",
)


def parse_sections(text: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    for heading, body in SECTION_RE.findall(text):
        sections.setdefault(heading, body.strip())
    return sections


def strip_code_ticks(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] == "`":
        return value[1:-1]
    return value


def parse_markdown_table_row(line: str) -> tuple[str, ...]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]

    cells: list[str] = []
    current: list[str] = []
    index = 0
    while index < len(stripped):
        character = stripped[index]
        if character == "\\" and index + 1 < len(stripped) and stripped[index + 1] == "|":
            current.append("|")
            index += 2
            continue
        if character == "|":
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(character)
        index += 1
    cells.append("".join(current).strip())
    return tuple(cells)


def parse_table_rows(section: str) -> list[tuple[str, ...]]:
    return [
        parse_markdown_table_row(line)
        for line in section.splitlines()
        if line.strip().startswith("|")
    ]


def table_has_data_row(rows: list[tuple[str, ...]]) -> bool:
    if len(rows) < 3:
        return False
    for cells in rows[2:]:
        if len(cells) == len(REVIEW_COLUMNS) and any(cells):
            return True
    return False


def validate_table_contract(
    rows: list[tuple[str, ...]], recommendations: str, evaluation: str
) -> list[str]:
    errors: list[str] = []
    claim_ids: list[str] = []
    implemented_claim_ids: list[str] = []
    for row_number, cells in enumerate(rows[2:], start=1):
        if len(cells) != len(REVIEW_COLUMNS):
            errors.append(
                f"Claim row {row_number} must have exactly {len(REVIEW_COLUMNS)} columns; "
                f"found {len(cells)}"
            )
            continue
        claim_match = CLAIM_ID_RE.match(cells[0])
        claim_id = ""
        if not claim_match:
            errors.append(f"Claim row {row_number} must start with a claim ID such as C01:")
        else:
            claim_id = claim_match.group(1).upper()
            claim_ids.append(claim_id)
        decision = cells[-2]
        implementation = cells[-1]
        if decision not in USER_DECISIONS:
            errors.append(
                f"Claim row {row_number} has invalid user decision: {cells[-2] or 'empty'}"
            )
        if implementation not in IMPLEMENTATION_STATUSES:
            errors.append(
                f"Claim row {row_number} has invalid implementation status: {cells[-1] or 'empty'}"
            )
        elif decision in STATUS_TRANSITIONS and implementation not in STATUS_TRANSITIONS[decision]:
            errors.append(
                f"Claim row {row_number} has inconsistent statuses: {decision} / {implementation}"
            )
        if claim_id and implementation == "implemented":
            implemented_claim_ids.append(claim_id)

    passed_evaluation_ids = {
        match.group(1).upper() for match in PASSED_EVALUATION_RE.finditer(evaluation)
    }
    for claim_id in implemented_claim_ids:
        if claim_id not in passed_evaluation_ids:
            errors.append(
                f"Implemented claim {claim_id} requires an evaluation line shaped "
                f"'- {claim_id}: passed - <verification command/result>'"
            )

    duplicates = sorted({claim_id for claim_id in claim_ids if claim_ids.count(claim_id) > 1})
    if duplicates:
        errors.append(f"Duplicate claim ID(s): {', '.join(duplicates)}")

    recommendation_ids = {match.upper() for match in ANY_CLAIM_ID_RE.findall(recommendations)}
    claim_id_set = set(claim_ids)
    missing_recommendations = sorted(claim_id_set - recommendation_ids)
    extra_recommendations = sorted(recommendation_ids - claim_id_set)
    if missing_recommendations:
        errors.append(
            "Recommendations section is missing claim ID(s): " + ", ".join(missing_recommendations)
        )
    if extra_recommendations:
        errors.append(
            "Recommendations section references unknown claim ID(s): "
            + ", ".join(extra_recommendations)
        )
    return errors


def find_sources_dir(card: Path) -> Path | None:
    for parent in card.parents:
        if parent.name == "sources" and parent.parent.name == "references":
            return parent
    return None


def resolve_within(candidate: Path, allowed_root: Path) -> tuple[Path, bool]:
    resolved_candidate = candidate.resolve()
    resolved_root = allowed_root.resolve()
    if ".." in candidate.parts:
        return resolved_candidate, False
    try:
        resolved_candidate.relative_to(resolved_root)
    except ValueError:
        return resolved_candidate, False
    return resolved_candidate, True


def snapshot_digest_and_trimmed_length(snapshot: Path) -> tuple[str, int]:
    digest = hashlib.sha256()
    total_length = 0
    leading_whitespace = 0
    trailing_whitespace = 0
    content_seen = False
    with snapshot.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
            total_length += len(chunk)
            if not content_seen:
                without_leading = chunk.lstrip()
                leading_whitespace += len(chunk) - len(without_leading)
                if not without_leading:
                    continue
                content_seen = True
                trailing_whitespace = len(without_leading) - len(without_leading.rstrip())
                continue
            without_trailing = chunk.rstrip()
            if without_trailing:
                trailing_whitespace = len(chunk) - len(without_trailing)
            else:
                trailing_whitespace += len(chunk)
    trimmed_length = total_length - leading_whitespace - trailing_whitespace
    return digest.hexdigest(), trimmed_length


def validate_snapshot(metadata: dict[str, str], sources_dir: Path) -> tuple[Path | None, list[str]]:
    errors: list[str] = []
    snapshot_value = strip_code_ticks(metadata.get("Snapshot", ""))
    if not snapshot_value:
        return None, errors

    candidate = Path(snapshot_value)
    unresolved_snapshot = candidate if candidate.is_absolute() else sources_dir / candidate
    snapshot, is_within_snapshots = resolve_within(
        unresolved_snapshot, sources_dir / "snapshots"
    )
    if not is_within_snapshots:
        errors.append("Snapshot must be stored under sources/snapshots/")
        return snapshot, errors

    if not snapshot.is_file():
        errors.append(f"Snapshot not found: {snapshot}")
        return snapshot, errors

    actual_hash, trimmed_length = snapshot_digest_and_trimmed_length(snapshot)
    if trimmed_length < 200:
        errors.append("Snapshot is too short to substantiate a complete full-text extraction")
    declared_hash = strip_code_ticks(metadata.get("Snapshot SHA-256", "")).lower()
    if not SHA256_RE.fullmatch(declared_hash):
        errors.append("Snapshot SHA-256 must be a 64-character hexadecimal digest")
    elif actual_hash != declared_hash:
        errors.append(
            "Snapshot SHA-256 does not match the saved snapshot "
            f"(declared {declared_hash}, actual {actual_hash})"
        )
    return snapshot, errors


def validate_text_integrity(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.is_file():
        return errors
    content = path.read_bytes()
    if any(marker in content for marker in CONFLICT_MARKERS):
        errors.append(f"Unresolved conflict marker in {path}")
    for line_number, line in enumerate(content.splitlines(), start=1):
        if line.endswith((b" ", b"\t")):
            errors.append(f"Trailing whitespace in {path}:{line_number}")
            break
    return errors


def validate_update_provenance(
    review_mode: str,
    section: str,
    sources_dir: Path,
    current_snapshot: Path | None,
    current_hash: str,
    current_identifier: str,
    current_retrieved: str,
) -> list[str]:
    errors: list[str] = []
    if review_mode == "new":
        if "initial ingestion" not in section.lower():
            errors.append("New-source Update provenance must state that this is the initial ingestion")
        return errors
    if review_mode != "update":
        return ["Review mode must be new or update"]

    rows = parse_table_rows(section)
    if not rows or rows[0] != UPDATE_PROVENANCE_COLUMNS:
        return ["Update provenance must contain the five-column previous/current table"]
    versions = {row[0].lower(): row for row in rows[2:] if len(row) == len(UPDATE_PROVENANCE_COLUMNS)}
    for required_version in ("previous", "current"):
        if required_version not in versions:
            errors.append(f"Update provenance is missing the {required_version} row")
    resolved_versions: dict[str, Path] = {}
    for version, row in versions.items():
        snapshot_value = strip_code_ticks(row[2])
        unresolved_snapshot_path = sources_dir / snapshot_value
        allowed_root = (
            sources_dir / "snapshots" / "archive"
            if version == "previous"
            else sources_dir / "snapshots"
        )
        snapshot_path, is_within_root = resolve_within(unresolved_snapshot_path, allowed_root)
        resolved_versions[version] = snapshot_path
        if not is_within_root:
            errors.append(
                "Previous update snapshot must be under snapshots/archive/"
                if version == "previous"
                else "Current update snapshot must be under snapshots/"
            )
            continue
        if not snapshot_path.is_file():
            errors.append(f"Update provenance {version} snapshot not found: {snapshot_path}")
            continue
        actual_hash, _ = snapshot_digest_and_trimmed_length(snapshot_path)
        declared_hash = strip_code_ticks(row[4]).lower()
        if actual_hash != declared_hash:
            errors.append(f"Update provenance {version} SHA-256 does not match its snapshot")
        if version == "current":
            if current_snapshot and snapshot_path.resolve() != current_snapshot.resolve():
                errors.append("Update provenance current snapshot does not match Metadata")
            if declared_hash != current_hash:
                errors.append("Update provenance current SHA-256 does not match Metadata")
            if strip_code_ticks(row[1]) != strip_code_ticks(current_identifier):
                errors.append("Update provenance current stable identifier does not match Metadata")
            if row[3] != current_retrieved:
                errors.append("Update provenance current retrieved date does not match Metadata")
    if (
        "previous" in resolved_versions
        and "current" in resolved_versions
        and resolved_versions["previous"] == resolved_versions["current"]
    ):
        errors.append("Update provenance previous and current snapshots must be distinct files")
    return errors


def validate_card(card: Path) -> list[str]:
    errors: list[str] = []
    if not card.is_file():
        return [f"Card not found: {card}"]

    sources_dir = find_sources_dir(card)
    if sources_dir is None:
        return ["Card must be inside dev/references/sources/"]

    text = card.read_text(encoding="utf-8")
    sections = parse_sections(text)

    for section in REQUIRED_SECTIONS:
        if section not in sections:
            errors.append(f"Missing required section: {section}")
        elif not sections[section]:
            errors.append(f"Required section is empty: {section}")

    placeholders = sorted(set(PLACEHOLDER_RE.findall(text)))
    if placeholders:
        errors.append(f"Unresolved template placeholder: {placeholders[0]}")

    metadata_section = sections.get("Metadata", "")
    metadata = {key.strip(): value.strip() for key, value in METADATA_RE.findall(metadata_section)}
    for field in REQUIRED_METADATA:
        value = metadata.get(field, "")
        if not value:
            errors.append(f"Missing or empty metadata field: {field}")

    full_text_status = metadata.get("Full-text status", "").strip().lower()
    if full_text_status != "complete":
        errors.append(
            "Full-text status must be complete before ingestion can pass; "
            f"found {full_text_status or 'missing'}"
        )

    snapshot, snapshot_errors = validate_snapshot(metadata, sources_dir)
    errors.extend(snapshot_errors)
    errors.extend(
        validate_update_provenance(
            metadata.get("Review mode", "").strip().lower(),
            sections.get("Update provenance", ""),
            sources_dir,
            snapshot,
            strip_code_ticks(metadata.get("Snapshot SHA-256", "")).lower(),
            metadata.get("Stable identifier", ""),
            metadata.get("Retrieved", ""),
        )
    )

    project_coverage = sections.get("Project coverage", "")
    table_rows = parse_table_rows(project_coverage)
    header = next((row for row in table_rows if row and row[0] == REVIEW_COLUMNS[0]), None)
    if header != REVIEW_COLUMNS:
        errors.append(
            "Project coverage must contain the authoritative seven-column review table "
            "from TEMPLATE.md"
        )
    elif len(table_rows) < 3:
        errors.append("Project coverage review table has no claim rows")
    else:
        errors.extend(
            validate_table_contract(
                table_rows,
                sections.get("Recommendations", ""),
                sections.get("Evaluation of approved changes", ""),
            )
        )

    document_review = sections.get("Document review", "")
    review_fields = {key.strip(): value.strip() for key, value in METADATA_RE.findall(document_review)}
    if review_fields.get("Review status", "").lower() != "passed":
        errors.append("Document review status must be passed")
    for field in ("Review method", "Findings resolved", "Unresolved findings"):
        if not review_fields.get(field):
            errors.append(f"Document review is missing: {field}")
    review_method = review_fields.get("Review method", "").strip().lower()
    if review_method and not review_method.startswith(REVIEW_METHOD_PREFIXES):
        errors.append(
            "Document review method must name an independent source-record reviewer "
            "or the explicit subagent-unavailable self-review fallback"
        )
    unresolved = review_fields.get("Unresolved findings", "").strip().lower().rstrip(".")
    if unresolved and unresolved not in {"none", "no unresolved findings"}:
        errors.append(f"Document review has unresolved findings: {review_fields['Unresolved findings']}")

    readme = sources_dir / "README.md"
    if not readme.is_file() or f"({card.name})" not in readme.read_text(encoding="utf-8"):
        errors.append("sources/README.md does not link to the card")

    manifest = sources_dir / "snapshots" / "MANIFEST.md"
    manifest_text = manifest.read_text(encoding="utf-8") if manifest.is_file() else ""
    manifest_row = next(
        (line for line in manifest_text.splitlines() if card.name in line),
        "",
    )
    if not manifest_row:
        errors.append("snapshots/MANIFEST.md does not list the card")
    else:
        manifest_values = (
            (metadata.get("URL", ""), "snapshots/MANIFEST.md does not include the source URL"),
            (snapshot.name if snapshot else "", "snapshots/MANIFEST.md does not include the snapshot path"),
            (
                metadata.get("Extraction method", ""),
                "snapshots/MANIFEST.md does not include the extraction method",
            ),
            (metadata.get("Retrieved", ""), "snapshots/MANIFEST.md does not include retrieval date"),
            (
                metadata.get("Stable identifier", ""),
                "snapshots/MANIFEST.md does not include the stable identifier",
            ),
            (
                strip_code_ticks(metadata.get("Snapshot SHA-256", "")),
                "snapshots/MANIFEST.md does not include the snapshot SHA-256",
            ),
            (
                metadata.get("Full-text status", ""),
                "snapshots/MANIFEST.md does not include the full-text status",
            ),
        )
        for value, message in manifest_values:
            if value and value not in manifest_row:
                errors.append(message)

    integrity_paths = [card]
    if snapshot:
        integrity_paths.append(snapshot)
    repo_root = sources_dir.parents[2]
    integrity_paths.extend(
        path
        for path in (
            readme,
            manifest,
            sources_dir / "pattern-opportunities.md",
            repo_root / "README.md",
        )
        if path.is_file()
    )
    for path in integrity_paths:
        errors.extend(validate_text_integrity(path))

    return errors


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate a newly ingested or updated human-eyes source card."
    )
    parser.add_argument("cards", nargs="+", type=Path, help="Source card path(s) to validate")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    failed = False
    for card in args.cards:
        errors = validate_card(card.resolve())
        if errors:
            failed = True
            print(f"FAIL {card.name}", file=sys.stderr)
            for error in errors:
                print(f"- {error}", file=sys.stderr)
        else:
            print(f"PASS {card.name}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
