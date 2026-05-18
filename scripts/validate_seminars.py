#!/usr/bin/env python3
"""Validate _data/seminars.yml against schema/seminar.schema.json."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "_data" / "seminars.yml"
SCHEMA_FILE = ROOT / "schema" / "seminar.schema.json"


def _normalize(data: object) -> object:
    """Coerce YAML types (e.g. dates) into JSON-schema-friendly values."""
    import datetime

    if isinstance(data, dict):
        return {k: _normalize(v) for k, v in data.items()}
    if isinstance(data, list):
        return [_normalize(v) for v in data]
    if isinstance(data, datetime.date) and not isinstance(data, datetime.datetime):
        return data.isoformat()
    return data


def main() -> int:
    try:
        import yaml
    except ImportError:
        print("ERROR: PyYAML required. Install with: pip install pyyaml", file=sys.stderr)
        return 1

    try:
        import jsonschema
    except ImportError:
        print(
            "ERROR: jsonschema required. Install with: pip install jsonschema",
            file=sys.stderr,
        )
        return 1

    if not DATA_FILE.is_file():
        print(f"ERROR: Missing {DATA_FILE}", file=sys.stderr)
        return 1

    with DATA_FILE.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)

    data = _normalize(data)

    with SCHEMA_FILE.open(encoding="utf-8") as f:
        schema = json.load(f)

    validator = jsonschema.Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path))

    if errors:
        print(f"Validation failed for {DATA_FILE}:", file=sys.stderr)
        for err in errors:
            path = ".".join(str(p) for p in err.absolute_path) or "(root)"
            print(f"  - {path}: {err.message}", file=sys.stderr)
        return 1

    seminars = data.get("seminars", [])
    ids = [s.get("id") for s in seminars]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        print(f"ERROR: Duplicate seminar ids: {', '.join(sorted(dupes))}", file=sys.stderr)
        return 1

    dates = [s.get("date", "") for s in seminars]
    if dates != sorted(dates):
        print(
            "WARNING: seminars are not sorted by date ascending "
            "(recommended for readability).",
            file=sys.stderr,
        )

    print(f"OK: {len(seminars)} seminar(s) validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
