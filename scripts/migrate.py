#!/usr/bin/env python3
"""
scripts/migrate.py
Converts original GTFOBins YAML entries to GTFOBins-Simplified format.

Usage:
    python3 migrate.py _old_gtfobins/_binaries/curl.md
    python3 migrate.py _old_gtfobins/_binaries/          # batch
    python3 migrate.py --dir _old_gtfobins/_binaries/ --out _binaries/

The original GTFOBins format uses Jekyll front-matter with a `functions`
list. This script maps those function names to the new capability vocabulary
and produces a stub YAML that you fill in with OPSEC/difficulty metadata.
"""

import argparse
import re
import sys
from pathlib import Path

import yaml  # pip install pyyaml

# Original GTFOBins function name → new capability list
FUNCTION_MAP = {
    "shell":         ["spawn", "exec"],
    "command":       ["exec"],
    "reverse-shell": ["reverse-shell", "exec"],
    "bind-shell":    ["bind", "exec"],
    "file-upload":   ["upload"],
    "file-download": ["download"],
    "file-read":     ["read"],
    "file-write":    ["write"],
    "library-load":  ["exec"],
    "sudo":          ["sudo"],
    "suid":          ["suid"],
    "capabilities":  ["exec"],
    "limited-suid":  ["suid"],
}

CAPABILITY_VOCAB = {
    "exec", "read", "write", "spawn", "upload",
    "download", "suid", "sudo", "bind", "reverse-shell"
}


def extract_frontmatter(text: str) -> dict:
    """Pull YAML front-matter from a Jekyll markdown file."""
    m = re.match(r"^---\n(.+?)\n---", text, re.DOTALL)
    if not m:
        raise ValueError("No front-matter found")
    return yaml.safe_load(m.group(1))


def map_capabilities(functions: list) -> list:
    caps = set()
    for fn in functions:
        fname = fn.get("function", "")
        mapped = FUNCTION_MAP.get(fname, [])
        caps.update(mapped)
    return sorted(caps, key=lambda c: list(CAPABILITY_VOCAB).index(c) if c in CAPABILITY_VOCAB else 99)


def build_examples(functions: list) -> list:
    examples = []
    for fn in functions:
        fname = fn.get("function", "unknown")
        caps = FUNCTION_MAP.get(fname, ["exec"])

        for i, ex in enumerate(fn.get("examples", [])):
            raw_cmd = ""
            for code in ex.get("code", []):
                if isinstance(code, dict) and code.get("type") == "command":
                    raw_cmd = code.get("command", "")
                    break

            examples.append({
                "id": f"{fname}-{i+1}" if i > 0 else fname,
                "description": ex.get("description", f"{fname} via {fname}"),
                "capabilities": caps,
                "command": raw_cmd.strip(),
                "notes": "",  # TO FILL
            })
    return examples


def convert(src: Path) -> dict:
    text = src.read_text(encoding="utf-8")
    fm = extract_frontmatter(text)

    functions = fm.get("functions", [])
    caps = map_capabilities(functions)
    examples = build_examples(functions)

    entry = {
        "name": src.stem,
        "capabilities": caps or ["exec"],
        "required_permissions": {
            "level": "user",
            "notes": "# TODO: verify",
        },
        "difficulty": "low",  # TODO: review
        "opsec": {
            "noise": "medium",  # TODO: review
            "artifacts": ["# TODO: list logs/files written"],
            "notes": "# TODO: add OPSEC notes",
        },
        "persistence_potential": False,  # TODO: review
        "examples": examples,
        "references": [
            f"https://gtfobins.github.io/gtfobins/{src.stem}/"
        ],
        "tags": [],
    }
    return entry


def dump_yaml(data: dict) -> str:
    return yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)


def main():
    parser = argparse.ArgumentParser(description="Migrate GTFOBins entries to Simplified format")
    parser.add_argument("source", nargs="?", help="Source .md file or directory")
    parser.add_argument("--dir", help="Source directory (batch mode)")
    parser.add_argument("--out", default="_binaries", help="Output directory (default: _binaries)")
    args = parser.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    sources = []
    if args.dir:
        sources = list(Path(args.dir).glob("*.md"))
    elif args.source:
        p = Path(args.source)
        sources = list(p.glob("*.md")) if p.is_dir() else [p]
    else:
        parser.print_help()
        sys.exit(1)

    for src in sources:
        try:
            entry = convert(src)
            out_path = out_dir / f"{src.stem}.yaml"
            out_path.write_text(dump_yaml(entry), encoding="utf-8")
            print(f"[OK] {src.name} → {out_path}")
        except Exception as e:
            print(f"[FAIL] {src.name}: {e}", file=sys.stderr)

    print(f"\nDone. Review TODO fields in {out_dir}/")
    print("Validate with: python3 scripts/validate.py _binaries/")


if __name__ == "__main__":
    main()
