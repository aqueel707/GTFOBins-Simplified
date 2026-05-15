#!/usr/bin/env python3
"""
scripts/migrate.py — GTFOBins upstream → GTFOBins-Simplified.

Handles:
  * Standard entries with functions: { ... }
  * Alias entries (alias: bash) → stub pointing at canonical
  * inherit function (binary chains via `from:`)
  * Per-context (sudo / suid / unprivileged / capabilities) variants
  * Comments at top-level and per-example
  * Multi-example functions
  * Sender/receiver/listener attributes for upload/download/shells

Usage:
    python3 scripts/migrate.py --dir path/to/upstream/_gtfobins/ --out _binaries/
"""

from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

import yaml


# ────────────────────────────────────────────────────────────────────────────
# Function name → new capability list
FUNCTION_MAP = {
    "shell":               ["spawn", "exec"],
    "command":             ["exec"],
    "reverse-shell":       ["reverse-shell", "exec"],
    "bind-shell":          ["bind", "exec"],
    "file-upload":         ["upload"],
    "upload":              ["upload"],
    "file-download":       ["download"],
    "download":            ["download"],
    "file-read":           ["read"],
    "file-write":          ["write"],
    "library-load":        ["exec"],
    "privilege-escalation":["exec", "suid"],
    "sudo":                ["sudo"],
    "suid":                ["suid"],
    "capabilities":        ["exec"],
    "limited-suid":        ["suid"],
    "non-interactive-reverse-shell": ["reverse-shell", "exec"],
    "non-interactive-bind-shell":    ["bind", "exec"],
}

# Default OPSEC noise per capability mix
NOISE_BY_CAP = {
    "reverse-shell": "high",
    "bind":          "high",
    "upload":        "medium",
    "download":      "medium",
    "exec":          "medium",
    "spawn":         "medium",
    "read":          "low",
    "write":         "low",
    "sudo":          "medium",
    "suid":          "low",
}

# Heuristic descriptions for each upstream function name
DESC = {
    "shell":         "Spawn an interactive shell.",
    "command":       "Execute an arbitrary command.",
    "reverse-shell": "Initiate a reverse shell to attacker host.",
    "bind-shell":    "Open a bind shell on a listening port.",
    "file-read":     "Read an arbitrary file.",
    "file-write":    "Write content to an arbitrary file.",
    "upload":        "Send a local file to a remote host.",
    "download":      "Fetch a remote file to disk.",
    "library-load":  "Load an arbitrary shared library.",
    "privilege-escalation": "Escalate to root via this binary.",
    "non-interactive-reverse-shell": "Non-interactive reverse shell.",
    "non-interactive-bind-shell":    "Non-interactive bind shell.",
}

# Persistence-relevant capabilities
PERSIST_CAPS = {"write", "exec", "spawn"}


# ────────────────────────────────────────────────────────────────────────────
def parse_upstream(text: str) -> dict:
    """Extract YAML front-matter or top-level YAML from an upstream file."""
    text = text.strip()
    # Some files are full front-matter, some are bare YAML
    if text.startswith("---"):
        # Strip ---\n at start and \n... or \n--- at end
        body = re.sub(r"^---\s*\n", "", text)
        body = re.sub(r"\n(\.\.\.|---)\s*$", "", body)
    else:
        body = text
    return yaml.safe_load(body) or {}


def extract_command(code_block) -> str:
    """An example's code might be a string or a dict-shaped variant."""
    if isinstance(code_block, str):
        return code_block.strip()
    if isinstance(code_block, dict):
        return str(code_block.get("code", "")).strip()
    return ""


def best_context_code(example: dict, fn_name: str) -> str:
    """Pick the most operator-relevant command from an upstream example."""
    base = example.get("code", "")
    # Prefer the unprivileged version; otherwise sudo; otherwise suid
    ctxs = example.get("contexts") or {}
    for ctx_name in ("unprivileged", "sudo", "suid"):
        if ctx_name in ctxs and isinstance(ctxs[ctx_name], dict):
            ctx_code = ctxs[ctx_name].get("code")
            if ctx_code:
                return str(ctx_code).strip()
    return str(base).strip()


def determine_perm_level(functions: dict) -> tuple[str, str]:
    """Find lowest-required permission across all functions.
    Returns (level, notes)."""
    has_unpriv = has_sudo = has_suid = has_cap = False
    for fn_list in functions.values():
        if not isinstance(fn_list, list):
            continue
        for ex in fn_list:
            ctxs = (ex.get("contexts") or {}) if isinstance(ex, dict) else {}
            if "unprivileged" in ctxs: has_unpriv = True
            if "sudo" in ctxs:         has_sudo = True
            if "suid" in ctxs:         has_suid = True
            if "capabilities" in ctxs: has_cap  = True

    if has_unpriv:
        return "user", ""
    if has_suid:
        return "suid", "Requires SUID bit set on the binary."
    if has_sudo:
        return "sudo", "Requires sudo rule for this binary."
    if has_cap:
        return "user", "Exploitable via Linux capabilities."
    return "user", ""


def determine_difficulty(functions: dict, name: str) -> str:
    """Heuristic difficulty based on payload complexity and version notes."""
    has_version = False
    multi_line_count = 0
    for fn_list in functions.values():
        if not isinstance(fn_list, list):
            continue
        for ex in fn_list:
            if not isinstance(ex, dict):
                continue
            if ex.get("version"):
                has_version = True
            code = ex.get("code", "")
            if isinstance(code, str) and code.count("\n") >= 3:
                multi_line_count += 1

    if has_version:
        return "medium"
    if multi_line_count >= 2:
        return "medium"
    return "low"


def collect_capabilities(functions: dict) -> list[str]:
    caps = set()
    for fn_name in functions:
        caps.update(FUNCTION_MAP.get(fn_name, []))
    # Preserve a stable display order
    order = ["exec", "spawn", "read", "write", "upload", "download",
             "bind", "reverse-shell", "suid", "sudo"]
    return [c for c in order if c in caps]


def determine_noise(caps: list[str]) -> str:
    """Worst-case noise across capabilities present."""
    levels = {"low": 0, "medium": 1, "high": 2}
    worst = 0
    for c in caps:
        n = NOISE_BY_CAP.get(c, "medium")
        if levels[n] > worst:
            worst = levels[n]
    return ["low", "medium", "high"][worst]


def default_artifacts(caps: list[str]) -> list[str]:
    arts = ["~/.bash_history"]
    if "reverse-shell" in caps or "bind" in caps:
        arts.append("Network connection logs / firewall logs")
        arts.append("auditd execve events")
    if "exec" in caps or "spawn" in caps:
        arts.append("Process arguments visible in ps and auditd")
    if "write" in caps:
        arts.append("File timestamps / inotify events on target paths")
    if "upload" in caps or "download" in caps:
        arts.append("Outbound network traffic to attacker host")
    return arts


def build_examples(functions: dict) -> list[dict]:
    examples = []
    seen_ids = set()
    for fn_name, fn_list in functions.items():
        if fn_name == "inherit":
            # Skip pure inherit; would chain to another binary
            continue
        if not isinstance(fn_list, list):
            continue
        for idx, ex in enumerate(fn_list):
            if not isinstance(ex, dict):
                continue
            cmd = best_context_code(ex, fn_name)
            if not cmd:
                continue
            base_id = fn_name if idx == 0 else f"{fn_name}-{idx+1}"
            ex_id = base_id
            c = 2
            while ex_id in seen_ids:
                ex_id = f"{base_id}-{c}"
                c += 1
            seen_ids.add(ex_id)
            example = {
                "id": ex_id,
                "description": DESC.get(fn_name, f"{fn_name} via this binary."),
                "capabilities": FUNCTION_MAP.get(fn_name, ["exec"]),
                "command": cmd,
            }
            if ex.get("comment"):
                example["notes"] = str(ex["comment"]).strip()
            examples.append(example)
    return examples


def convert(src: Path) -> dict | None:
    """Return the new-format dict, or None to skip (e.g. unparseable)."""
    text = src.read_text(encoding="utf-8")
    try:
        data = parse_upstream(text)
    except yaml.YAMLError:
        return None

    # Alias → stub
    if "alias" in data:
        return {
            "name": src.name,
            "capabilities": ["exec"],
            "required_permissions": {"level": "user", "notes": f"Alias of `{data['alias']}` — see that entry for details."},
            "difficulty": "low",
            "opsec": {"noise": "low", "artifacts": [], "notes": f"Identical behavior to `{data['alias']}`."},
            "persistence_potential": False,
            "examples": [{
                "id": "alias",
                "description": f"This binary aliases to `{data['alias']}`.",
                "capabilities": ["exec"],
                "command": f"# See _binaries/{data['alias']}.md for usage",
            }],
            "references": [f"https://gtfobins.github.io/gtfobins/{src.name}/"],
            "tags": ["alias"],
        }

    functions = data.get("functions") or {}
    if not isinstance(functions, dict) or not functions:
        return None

    # If only inherit functions exist, create a chain-stub entry
    non_inherit = {k: v for k, v in functions.items() if k != "inherit"}
    if not non_inherit and "inherit" in functions:
        inherit_list = functions["inherit"]
        parents, examples = set(), []
        if isinstance(inherit_list, list):
            for idx, ex in enumerate(inherit_list):
                if not isinstance(ex, dict): continue
                parent = ex.get("from", "")
                if parent: parents.add(parent)
                cmd = str(ex.get("code", "")).strip()
                if cmd:
                    examples.append({
                        "id": f"inherit-{idx+1}" if idx > 0 else "inherit",
                        "description": f"Inherits attack surface from `{parent}` — see that entry.",
                        "capabilities": ["exec"],
                        "command": cmd,
                        "notes": str(ex.get("comment", "")).strip(),
                    })
        parents_str = ", ".join(sorted(parents)) if parents else "another binary"
        return {
            "name": src.name,
            "capabilities": ["exec"],
            "required_permissions": {"level": "user",
                "notes": f"Inherits behavior from {parents_str}."},
            "difficulty": "low",
            "opsec": {"noise": "medium",
                "artifacts": ["~/.bash_history"],
                "notes": f"Chains to {parents_str}; OPSEC follows that binary's profile."},
            "persistence_potential": False,
            "examples": examples or [{
                "id": "inherit",
                "description": f"Chains to `{parents_str}`.",
                "capabilities": ["exec"],
                "command": f"# See _binaries/{sorted(parents)[0]}.md" if parents else "# See parent binary",
            }],
            "references": [f"https://gtfobins.github.io/gtfobins/{src.name}/"],
            "tags": ["inherit"] + sorted(parents),
        }

    caps = collect_capabilities(functions)
    if not caps:
        caps = ["exec"]

    level, perm_notes = determine_perm_level(functions)
    difficulty = determine_difficulty(functions, src.name)
    examples = build_examples(functions)
    if not examples:
        return None

    noise = determine_noise(caps)
    persist = bool(set(caps) & PERSIST_CAPS) and ("write" in caps or "exec" in caps)

    entry = {
        "name": src.name,
        "capabilities": caps,
        "required_permissions": {"level": level, "notes": perm_notes} if perm_notes
                                 else {"level": level},
        "difficulty": difficulty,
        "opsec": {
            "noise": noise,
            "artifacts": default_artifacts(caps),
            "notes": str(data.get("comment", "")).strip() if data.get("comment") else "",
        },
        "persistence_potential": persist,
        "examples": examples,
        "references": [f"https://gtfobins.github.io/gtfobins/{src.name}/"],
        "tags": [],
    }
    if persist:
        entry["persistence_notes"] = "Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units."
    return entry


class NoAliasDumper(yaml.SafeDumper):
    """Prevent YAML from emitting anchors/aliases for repeated objects."""
    def ignore_aliases(self, data):
        return True


def _str_representer(dumper, data):
    """Use literal block style (|) for multi-line strings."""
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


NoAliasDumper.add_representer(str, _str_representer)


def dump_frontmatter(entry: dict) -> str:
    body = yaml.dump(entry, Dumper=NoAliasDumper, default_flow_style=False,
                     allow_unicode=True, sort_keys=False, width=1000)
    return f"---\n{body}---\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True, help="Upstream _gtfobins/ directory")
    ap.add_argument("--out", required=True, help="Output _binaries/ directory")
    args = ap.parse_args()

    src_dir = Path(args.dir)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    files = sorted(src_dir.glob("*"))
    ok = skipped = failed = 0
    for f in files:
        if not f.is_file():
            continue
        try:
            entry = convert(f)
            if entry is None:
                skipped += 1
                continue
            out_path = out_dir / f"{f.name}.md"
            out_path.write_text(dump_frontmatter(entry), encoding="utf-8")
            ok += 1
        except Exception as e:
            print(f"[FAIL] {f.name}: {e}", file=sys.stderr)
            failed += 1

    print(f"\n{ok} converted, {skipped} skipped, {failed} failed.")
    print(f"Output: {out_dir}/")


if __name__ == "__main__":
    main()
