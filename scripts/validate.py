#!/usr/bin/env python3
"""
scripts/validate.py
Validates all YAML entries in _binaries/ against binary.schema.json.

Usage:
    python3 scripts/validate.py _binaries/
    python3 scripts/validate.py _binaries/curl.yaml

Requires:
    pip install pyyaml jsonschema
"""

import json
import sys
from pathlib import Path

import yaml
from jsonschema import validate, ValidationError

SCHEMA_PATH = Path(__file__).parent.parent / "schema" / "binary.schema.json"


def main():
    schema = json.loads(SCHEMA_PATH.read_text())
    targets = []

    if len(sys.argv) < 2:
        print("Usage: validate.py <file.yaml | directory>")
        sys.exit(1)

    p = Path(sys.argv[1])
    targets = list(p.glob("*.yaml")) if p.is_dir() else [p]

    passed = failed = 0
    for path in sorted(targets):
        data = yaml.safe_load(path.read_text())
        try:
            validate(instance=data, schema=schema)
            print(f"[PASS] {path.name}")
            passed += 1
        except ValidationError as e:
            print(f"[FAIL] {path.name}: {e.message} (at {list(e.absolute_path)})")
            failed += 1

    print(f"\n{passed} passed, {failed} failed out of {passed+failed} entries.")
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
