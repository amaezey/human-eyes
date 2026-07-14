import hashlib
import importlib.util
import io
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = REPO_ROOT / ".agents" / "skills" / "source-ingest" / "scripts" / "validate_source.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_source", VALIDATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


VALIDATOR = load_validator()


class SourceIngestionValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp_dir.name)
        self.sources = self.repo / "human-eyes" / "references" / "sources"
        self.snapshots = self.sources / "snapshots"
        self.snapshots.mkdir(parents=True)

    def tearDown(self):
        self.temp_dir.cleanup()

    def write_valid_record(self):
        snapshot_text = (
            "# Example source\n\n"
            "Original URL: https://example.com/source\n"
            "Retrieved: 2026-07-14\n\n"
            "## Full text\n\n"
            + ("This is preserved source text with complete claims and examples. " * 12).strip()
        )
        snapshot = self.snapshots / "example-source.md"
        snapshot.write_text(snapshot_text, encoding="utf-8")
        digest = hashlib.sha256(snapshot.read_bytes()).hexdigest()

        card = self.sources / "example-source.md"
        card.write_text(
            f"""# Example source

## Metadata

- **URL:** https://example.com/source
- **Author / owner:** Example Author
- **Published:** 2026-07-01
- **Retrieved:** 2026-07-14
- **Extracted:** 2026-07-14
- **Source type:** Controlled experiment
- **Evidence tier:** Peer-reviewed / academic empirical
- **Review mode:** new
- **Stable identifier:** DOI 10.0000/example
- **Version / revision:** Version 2
- **Full-text status:** complete
- **Snapshot:** `snapshots/example-source.md`
- **Extraction method:** direct HTML article extraction
- **Snapshot SHA-256:** `{digest}`
- **Model / corpus scope:** Model X; 100 English essays from 2026
- **Access limitations:** none

## Summary

The source compares measured writing patterns and supplies direct evidence.

## Main insights

- The measured pattern varies by genre.

## Evidence and claims to extract

- **Direct source reviewed:** complete article.
- **Method and sample:** controlled comparison of 100 essays.
- **Direct versus cited evidence:** C01 is measured by this source.
- **Important limits and counterexamples:** English essays only.

## Skill-use audit

- **Good use:** Aggregate, genre-scoped evidence.
- **Misuse / overclaim:** Individual authorship classification.
- **Unsupported use:** Other languages.
- **Underused evidence:** Genre controls.
- **Patterns left on the table:** None.

## Matched patterns / rules

- #7 AI vocabulary words and phrases

## Associated hypotheses

- H12 genre-aware threshold calibration

## Questions / follow-up

- None.

## Update provenance

- Not applicable: initial ingestion.

## Decision history

- None: initial review.

## Project coverage

| Source claim or example | Evidence assessment | Existing project coverage | Missing or challenged | Recommendation | User decision | Implementation status |
|---|---|---|---|---|---|---|
| C01: Pattern frequency changes by genre. | Direct controlled comparison; bounded to the sample. | H12 covers genre calibration. | No matching fixture. | Add an evaluation fixture. | pending | not started |

## Recommendations

- C01: Add an evaluation fixture after approval; do not change a detector threshold yet.

## Evaluation of approved changes

- Not applicable while C01 is pending.

## Document review

- **Review status:** passed
- **Review method:** independent source-record reviewer: reviewer-1
- **Findings resolved:** Full-text scope and project coverage were checked.
- **Unresolved findings:** none
""",
            encoding="utf-8",
        )

        (self.sources / "README.md").write_text(
            "# Sources\n\n- [Example source](example-source.md)\n", encoding="utf-8"
        )
        (self.snapshots / "MANIFEST.md").write_text(
            "| Source card | Original URL | Snapshot | Method | Retrieved | Stable identifier | SHA-256 | Full-text status |\n"
            "|---|---|---|---|---|---|---|---|\n"
            f"| [`example-source.md`](../example-source.md) | https://example.com/source | "
            f"[`snapshots/example-source.md`](example-source.md) | direct HTML article extraction | "
            f"2026-07-14 | DOI 10.0000/example | `{digest}` | complete |\n",
            encoding="utf-8",
        )
        return card, snapshot

    def make_valid_update(self, card, snapshot):
        archive = self.snapshots / "archive" / "example-source" / "2026-06-01-revision-1.md"
        archive.parent.mkdir(parents=True)
        archive.write_text(
            "# Previous source revision\n\n" + ("Earlier reviewed source text. " * 16).strip(),
            encoding="utf-8",
        )
        previous_digest = hashlib.sha256(archive.read_bytes()).hexdigest()
        current_digest = hashlib.sha256(snapshot.read_bytes()).hexdigest()
        text = card.read_text(encoding="utf-8")
        text = text.replace("**Review mode:** new", "**Review mode:** update")
        text = text.replace(
            "- Not applicable: initial ingestion.",
            "| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |\n"
            "|---|---|---|---|---|\n"
            "| previous | revision 1 | "
            "`snapshots/archive/example-source/2026-06-01-revision-1.md` | "
            f"2026-06-01 | `{previous_digest}` |\n"
            "| current | DOI 10.0000/example | `snapshots/example-source.md` | "
            f"2026-07-14 | `{current_digest}` |",
            1,
        )
        card.write_text(text, encoding="utf-8")
        return archive

    def validate(self, card):
        stdout = io.StringIO()
        stderr = io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            exit_code = VALIDATOR.main([str(card)])
        return exit_code, stdout.getvalue(), stderr.getvalue()

    def test_accepts_complete_record(self):
        card, _ = self.write_valid_record()

        exit_code, stdout, stderr = self.validate(card)

        self.assertEqual(0, exit_code, stderr)
        self.assertIn("PASS example-source.md", stdout)

    def test_repository_template_matches_validator_contract(self):
        template = (REPO_ROOT / "human-eyes" / "references" / "sources" / "TEMPLATE.md").read_text(
            encoding="utf-8"
        )
        sections = VALIDATOR.parse_sections(template)
        metadata = {
            key.strip(): value.strip()
            for key, value in VALIDATOR.METADATA_RE.findall(sections["Metadata"])
        }
        rows = VALIDATOR.parse_table_rows(sections["Project coverage"])

        self.assertTrue(set(VALIDATOR.REQUIRED_SECTIONS).issubset(sections))
        self.assertTrue(set(VALIDATOR.REQUIRED_METADATA).issubset(metadata))
        self.assertIn(VALIDATOR.REVIEW_COLUMNS, rows)

    def test_rejects_snapshot_hash_mismatch(self):
        card, snapshot = self.write_valid_record()
        snapshot.write_text(snapshot.read_text(encoding="utf-8") + "changed", encoding="utf-8")

        exit_code, _, stderr = self.validate(card)

        self.assertEqual(1, exit_code)
        self.assertIn("Snapshot SHA-256 does not match", stderr)

    def test_rejects_snapshot_parent_traversal(self):
        outside = self.sources / "outside.md"
        outside.write_text("Outside the snapshot root. " * 16, encoding="utf-8")
        digest = hashlib.sha256(outside.read_bytes()).hexdigest()

        _, errors = VALIDATOR.validate_snapshot(
            {
                "Snapshot": "snapshots/../outside.md",
                "Snapshot SHA-256": digest,
            },
            self.sources,
        )

        self.assertIn("Snapshot must be stored under sources/snapshots/", errors)

    def test_rejects_snapshot_symlink_escape(self):
        outside = self.sources / "outside.md"
        outside.write_text("Outside the snapshot root. " * 16, encoding="utf-8")
        symlink = self.snapshots / "escape.md"
        symlink.symlink_to(outside)
        digest = hashlib.sha256(outside.read_bytes()).hexdigest()

        _, errors = VALIDATOR.validate_snapshot(
            {
                "Snapshot": "snapshots/escape.md",
                "Snapshot SHA-256": digest,
            },
            self.sources,
        )

        self.assertIn("Snapshot must be stored under sources/snapshots/", errors)

    def test_rejects_incomplete_full_text(self):
        card, _ = self.write_valid_record()
        text = card.read_text(encoding="utf-8").replace(
            "**Full-text status:** complete", "**Full-text status:** partial"
        )
        card.write_text(text, encoding="utf-8")

        exit_code, _, stderr = self.validate(card)

        self.assertEqual(1, exit_code)
        self.assertIn("Full-text status must be complete", stderr)

    def test_rejects_missing_manifest_and_readme_entries(self):
        card, _ = self.write_valid_record()
        (self.sources / "README.md").write_text("# Sources\n", encoding="utf-8")
        (self.snapshots / "MANIFEST.md").write_text("# Manifest\n", encoding="utf-8")

        exit_code, _, stderr = self.validate(card)

        self.assertEqual(1, exit_code)
        self.assertIn("sources/README.md does not link to the card", stderr)
        self.assertIn("snapshots/MANIFEST.md does not list the card", stderr)

    def test_manifest_provenance_must_be_on_the_card_row(self):
        card, _ = self.write_valid_record()
        manifest = self.snapshots / "MANIFEST.md"
        text = manifest.read_text(encoding="utf-8")
        text = text.replace("direct HTML article extraction", "browser copy")
        text += "\nThe archive also supports direct HTML article extraction.\n"
        manifest.write_text(text, encoding="utf-8")

        exit_code, _, stderr = self.validate(card)

        self.assertEqual(1, exit_code)
        self.assertIn("does not include the extraction method", stderr)

    def test_rejects_integrity_failure_in_project_indexes(self):
        card, _ = self.write_valid_record()
        pattern_opportunities = self.sources / "pattern-opportunities.md"
        pattern_opportunities.write_text("# Opportunities\n\n<<<<<<< ours\n", encoding="utf-8")

        exit_code, _, stderr = self.validate(card)

        self.assertEqual(1, exit_code)
        self.assertIn("Unresolved conflict marker", stderr)

    def test_rejects_unresolved_document_review(self):
        card, _ = self.write_valid_record()
        text = card.read_text(encoding="utf-8").replace(
            "**Unresolved findings:** none", "**Unresolved findings:** Verify the sample size."
        )
        card.write_text(text, encoding="utf-8")

        exit_code, _, stderr = self.validate(card)

        self.assertEqual(1, exit_code)
        self.assertIn("Document review has unresolved findings", stderr)

    def test_rejects_unidentified_review_method(self):
        card, _ = self.write_valid_record()
        text = card.read_text(encoding="utf-8").replace(
            "**Review method:** independent source-record reviewer: reviewer-1",
            "**Review method:** general final check",
        )
        card.write_text(text, encoding="utf-8")

        exit_code, _, stderr = self.validate(card)

        self.assertEqual(1, exit_code)
        self.assertIn("must name an independent source-record reviewer", stderr)

    def test_accepts_explicit_self_review_fallback(self):
        card, _ = self.write_valid_record()
        text = card.read_text(encoding="utf-8").replace(
            "**Review method:** independent source-record reviewer: reviewer-1",
            "**Review method:** self-review fallback: subagents unavailable",
        )
        card.write_text(text, encoding="utf-8")

        exit_code, _, stderr = self.validate(card)

        self.assertEqual(0, exit_code, stderr)

    def test_rejects_noncanonical_statuses(self):
        card, _ = self.write_valid_record()
        text = card.read_text(encoding="utf-8")
        text = text.replace("| pending | not started |", "| maybe | done |")
        card.write_text(text, encoding="utf-8")

        exit_code, _, stderr = self.validate(card)

        self.assertEqual(1, exit_code)
        self.assertIn("invalid user decision: maybe", stderr)
        self.assertIn("invalid implementation status: done", stderr)

    def test_rejects_mixed_case_statuses(self):
        card, _ = self.write_valid_record()
        text = card.read_text(encoding="utf-8")
        text = text.replace("| pending | not started |", "| Pending | Not Started |")
        card.write_text(text, encoding="utf-8")

        exit_code, _, stderr = self.validate(card)

        self.assertEqual(1, exit_code)
        self.assertIn("invalid user decision: Pending", stderr)
        self.assertIn("invalid implementation status: Not Started", stderr)

    def test_accepts_escaped_pipe_in_claim_cell(self):
        card, _ = self.write_valid_record()
        text = card.read_text(encoding="utf-8").replace(
            "C01: Pattern frequency changes by genre.",
            r"C01: Pattern \| frequency changes by genre.",
            1,
        )
        card.write_text(text, encoding="utf-8")

        exit_code, _, stderr = self.validate(card)

        self.assertEqual(0, exit_code, stderr)

    def test_rejects_malformed_project_coverage_widths(self):
        malformed_rows = (
            "| C02: Too few cells. | only one more |",
            "| C02: Unescaped | pipe | adds | too | many | cells | here | extra |",
        )
        for malformed_row in malformed_rows:
            with self.subTest(row=malformed_row):
                card, _ = self.write_valid_record()
                text = card.read_text(encoding="utf-8").replace(
                    "| C01: Pattern frequency changes by genre.",
                    malformed_row + "\n| C01: Pattern frequency changes by genre.",
                    1,
                )
                card.write_text(text, encoding="utf-8")

                exit_code, _, stderr = self.validate(card)

                self.assertEqual(1, exit_code)
                self.assertIn("must have exactly 7 columns", stderr)

    def test_rejects_claim_without_id_or_matching_recommendation(self):
        card, _ = self.write_valid_record()
        text = card.read_text(encoding="utf-8")
        text = text.replace("C01: Pattern frequency", "Pattern frequency", 1)
        card.write_text(text, encoding="utf-8")

        exit_code, _, stderr = self.validate(card)

        self.assertEqual(1, exit_code)
        self.assertIn("must start with a claim ID", stderr)
        self.assertIn("unknown claim ID(s): C01", stderr)

    def test_rejects_update_without_archived_previous_snapshot(self):
        card, snapshot = self.write_valid_record()
        digest = hashlib.sha256(snapshot.read_bytes()).hexdigest()
        text = card.read_text(encoding="utf-8")
        text = text.replace("**Review mode:** new", "**Review mode:** update")
        text = text.replace(
            "- Not applicable: initial ingestion.",
            "| Version | Stable identifier | Snapshot | Retrieved | SHA-256 |\n"
            "|---|---|---|---|---|\n"
            "| previous | revision 1 | `snapshots/archive/example-source/2026-06-01-old.md` | 2026-06-01 | `"
            + ("0" * 64)
            + "` |\n"
            "| current | DOI 10.0000/example | `snapshots/example-source.md` | 2026-07-14 | `"
            + digest
            + "` |",
        )
        card.write_text(text, encoding="utf-8")

        exit_code, _, stderr = self.validate(card)

        self.assertEqual(1, exit_code)
        self.assertIn("previous snapshot not found", stderr)

    def test_accepts_valid_update_provenance(self):
        card, snapshot = self.write_valid_record()
        self.make_valid_update(card, snapshot)

        exit_code, stdout, stderr = self.validate(card)

        self.assertEqual(0, exit_code, stderr)
        self.assertIn("PASS example-source.md", stdout)

    def test_rejects_current_update_metadata_mismatch(self):
        card, snapshot = self.write_valid_record()
        self.make_valid_update(card, snapshot)
        text = card.read_text(encoding="utf-8")
        text = text.replace(
            "| current | DOI 10.0000/example | `snapshots/example-source.md` | 2026-07-14 |",
            "| current | DOI 10.0000/different | `snapshots/example-source.md` | 2026-07-15 |",
        )
        card.write_text(text, encoding="utf-8")

        exit_code, _, stderr = self.validate(card)

        self.assertEqual(1, exit_code)
        self.assertIn("current stable identifier does not match Metadata", stderr)
        self.assertIn("current retrieved date does not match Metadata", stderr)

    def test_rejects_archive_parent_traversal(self):
        card, snapshot = self.write_valid_record()
        archive = self.make_valid_update(card, snapshot)
        outside = self.sources / "outside.md"
        outside.write_bytes(archive.read_bytes())
        digest = hashlib.sha256(outside.read_bytes()).hexdigest()
        text = card.read_text(encoding="utf-8")
        text = text.replace(
            "`snapshots/archive/example-source/2026-06-01-revision-1.md`",
            "`snapshots/archive/../../outside.md`",
        ).replace(hashlib.sha256(archive.read_bytes()).hexdigest(), digest)
        card.write_text(text, encoding="utf-8")

        exit_code, _, stderr = self.validate(card)

        self.assertEqual(1, exit_code)
        self.assertIn("Previous update snapshot must be under snapshots/archive/", stderr)

    def test_rejects_previous_current_resolved_path_alias(self):
        card, snapshot = self.write_valid_record()
        archive = self.make_valid_update(card, snapshot)
        archive.unlink()
        archive.symlink_to(snapshot)
        current_digest = hashlib.sha256(snapshot.read_bytes()).hexdigest()
        text = card.read_text(encoding="utf-8")
        previous_digest = next(
            cell.strip("` ")
            for cell in text.split("| previous |", 1)[1].split("\n", 1)[0].split("|")
            if len(cell.strip("` ")) == 64
        )
        card.write_text(text.replace(previous_digest, current_digest), encoding="utf-8")

        exit_code, _, stderr = self.validate(card)

        self.assertEqual(1, exit_code)
        self.assertIn("previous and current snapshots must be distinct files", stderr)

    def test_rejects_inconsistent_status_transition(self):
        card, _ = self.write_valid_record()
        text = card.read_text(encoding="utf-8").replace(
            "| pending | not started |", "| rejected | implemented |"
        )
        card.write_text(text, encoding="utf-8")

        exit_code, _, stderr = self.validate(card)

        self.assertEqual(1, exit_code)
        self.assertIn("inconsistent statuses: rejected / implemented", stderr)

    def test_accepts_mixed_implemented_and_pending_outcomes(self):
        card, _ = self.write_valid_record()
        text = card.read_text(encoding="utf-8")
        text = text.replace(
            "| C01: Pattern frequency changes by genre. | Direct controlled comparison; bounded to the sample. | H12 covers genre calibration. | No matching fixture. | Add an evaluation fixture. | pending | not started |",
            "| C01: Pattern frequency changes by genre. | Direct controlled comparison; bounded to the sample. | H12 covers genre calibration. | No matching fixture. | Add an evaluation fixture. | approved | implemented |\n"
            "| C02: Record a bounded observation. | Direct observation. | Existing guidance covers it. | None. | Take no further action. | pending | not started |",
        )
        text = text.replace(
            "- C01: Add an evaluation fixture after approval; do not change a detector threshold yet.",
            "- C01: Add an evaluation fixture after approval; do not change a detector threshold yet.\n"
            "- C02: Take no further action.",
        )
        text = text.replace(
            "- Not applicable while C01 is pending.",
            "- C01: passed - `python3 dev/evals/tests/test_source_ingestion.py` returned OK.\n"
            "- C02: Not applicable while the recommendation remains pending.",
        )
        card.write_text(text, encoding="utf-8")

        exit_code, _, stderr = self.validate(card)

        self.assertEqual(0, exit_code, stderr)

    def test_rejects_implemented_claim_without_keyed_evaluation(self):
        card, _ = self.write_valid_record()
        text = card.read_text(encoding="utf-8")
        text = text.replace("| pending | not started |", "| approved | implemented |")
        text = text.replace(
            "- Not applicable while C01 is pending.",
            "- Tests passed successfully.",
        )
        card.write_text(text, encoding="utf-8")

        exit_code, _, stderr = self.validate(card)

        self.assertEqual(1, exit_code)
        self.assertIn("Implemented claim C01 requires an evaluation line", stderr)

    def test_rejects_missing_required_section_and_placeholder(self):
        card, _ = self.write_valid_record()
        text = card.read_text(encoding="utf-8")
        text = text.replace("## Main insights", "## Observations")
        text = text.replace("Example Author", "<author>")
        card.write_text(text, encoding="utf-8")

        exit_code, _, stderr = self.validate(card)

        self.assertEqual(1, exit_code)
        self.assertIn("Missing required section: Main insights", stderr)
        self.assertIn("Unresolved template placeholder", stderr)


if __name__ == "__main__":
    unittest.main()
