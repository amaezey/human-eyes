#!/usr/bin/env python3
"""Detection-type consistency: registries are the truth, prose must match.

Every catalogue entry must carry exactly one derived Detection line, and the
root README's Check column must agree with the same derivation.
"""

import importlib.util
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
_spec = importlib.util.spec_from_file_location(
    "render_patterns_md", ROOT / "dev" / "tools" / "render_patterns_md.py")
_rpm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_rpm)

README_ROW_RE = re.compile(r"^\| ([A-Z]\d+) \| [^|]+\| [^|]+\| (\w+) \|", re.M)


def derived_short_form(number, slug, programmatic, judgement_by_number):
    stem = _rpm.derive_detection(number, slug, programmatic, judgement_by_number)
    if stem.startswith(("Programmatic", "Folded")):
        return "regex"
    if stem.startswith("Agent judgement"):
        return "agent"
    return "manual"


class DetectionMarkerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.programmatic, cls.judgement = _rpm._load_detection_registries()
        import json
        data = json.loads(_rpm.PATTERNS_JSON.read_text())
        cls.slug_by_number = {
            rec["pattern_number"]: cid for cid, rec in data.items()
            if not cid.startswith("_") and "pattern_number" in rec}
        for entry in data.get("_extra_entries", []):
            cls.slug_by_number.setdefault(entry["pattern_number"], None)

    def test_every_catalogue_entry_has_one_detection_line(self):
        text = _rpm.PATTERNS_MD.read_text()
        for m in re.finditer(r"^### ([A-Z]\d+)\.[^\n]*\n(.*?)(?=^### |^## |\Z)",
                             text, re.M | re.S):
            count = m.group(2).count("**Detection:**")
            self.assertEqual(1, count, f"entry {m.group(1)} has {count} Detection lines")

    def test_readme_check_column_matches_registries(self):
        text = (ROOT / "README.md").read_text()
        rows = README_ROW_RE.findall(text)
        self.assertGreater(len(rows), 40, "README pattern table not found")
        for number, check in rows:
            slug = self.slug_by_number.get(number)
            expected = derived_short_form(number, slug, self.programmatic, self.judgement)
            self.assertEqual(
                expected, check,
                f"README row {number} says '{check}' but registries derive '{expected}'")


if __name__ == "__main__":
    unittest.main(verbosity=1)
