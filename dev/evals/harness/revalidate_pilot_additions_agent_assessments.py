#!/usr/bin/env python3
"""Rebind retained pilot-addition agent answers to the current grader.

The prior answers remain identifiable as retained agent judgments. This script
does not change them; it creates fresh work bundles, validates all 15 answers
through the current native Audit path, and writes a document identity index.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DEFAULT_MANIFEST = ROOT / "dev/evals/samples/pilot-additions-01/manifest.json"
DEFAULT_SOURCE = ROOT / "dev/evals/three-version-native-audits/pilot-additions/current/annotator-a"
DEFAULT_OUTPUT = ROOT / "dev/evals/three-version-native-audits/pilot-additions/updated-current"
GRADER = ROOT / "human-eyes/scripts/grade.py"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve(value: str, manifest_path: Path) -> Path:
    path = (manifest_path.parent / value).resolve()
    if not path.is_file():
        raise FileNotFoundError(path)
    return path


def source_bundles(directory: Path) -> dict[str, tuple[Path, list[dict]]]:
    result = {}
    for path in sorted(directory.glob("*.json")):
        bundle = json.loads(path.read_text(encoding="utf-8"))
        content_hash = bundle.get("bindings", {}).get("content_sha256")
        answers = bundle.get("semantic_answers")
        if not isinstance(content_hash, str) or not isinstance(answers, list) or len(answers) != 15:
            raise ValueError(f"invalid retained agent-answer bundle: {path}")
        if content_hash in result:
            raise ValueError(f"duplicate retained content hash: {content_hash}")
        result[content_hash] = (path, answers)
    return result


def run(manifest_path: Path, source_dir: Path, output_dir: Path) -> dict:
    manifest_path = manifest_path.resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    retained = source_bundles(source_dir.resolve())
    bundle_dir = output_dir / "work-bundles"
    audit_dir = output_dir / "audits"
    bundle_dir.mkdir(parents=True, exist_ok=True)
    audit_dir.mkdir(parents=True, exist_ok=True)
    records = []
    for pair in manifest["pairs"]:
        for cohort in ("human", "ai"):
            document = resolve(pair[cohort]["path"], manifest_path)
            content_hash = digest(document)
            if content_hash not in retained:
                raise ValueError(f"no retained semantic answers for {pair['id']}::{cohort}")
            source_path, answers = retained[content_hash]
            document_id = f"{pair['id']}::{cohort}"
            stem = document_id.replace("::", "--")
            bundle_path = bundle_dir / f"{stem}.json"
            audit_path = audit_dir / f"{stem}.json"
            subprocess.run(
                [sys.executable, str(GRADER), "preflight", str(document),
                 "--work-bundle", str(bundle_path)],
                cwd=ROOT, check=True, stdout=subprocess.DEVNULL,
            )
            bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
            bundle["semantic_answers"] = answers
            bundle_path.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(GRADER), "audit", str(document),
                 "--work-bundle", str(bundle_path), "--format", "json"],
                cwd=ROOT, check=True, text=True, stdout=subprocess.PIPE,
            )
            audit = json.loads(result.stdout)
            if audit.get("coverage_mode") != "full" or audit.get("audit_status") != "complete":
                raise ValueError(f"current audit incomplete for {document_id}")
            if len(audit.get("semantic_findings", [])) != 15:
                raise ValueError(f"current audit lacks 15 semantic findings for {document_id}")
            audit_path.write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            records.append({
                "document_id": document_id,
                "cohort": cohort,
                "path": str(document),
                "content_sha256": content_hash,
                "retained_answers_from": str(source_path),
                "work_bundle": str(bundle_path),
                "audit": str(audit_path),
            })
    index = {"schema_version": 1, "manifest": str(manifest_path), "documents": records}
    (output_dir / "index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return index


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    try:
        index = run(args.manifest, args.source, args.output)
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(json.dumps({"documents": len(index["documents"]), "output": str(args.output)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
