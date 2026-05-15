# Contributing to GTFOBins-Simplified

## PR Checklist

- [ ] `_binaries/<name>.yaml` matches `name` field exactly
- [ ] All required fields present (no `# TODO` markers)
- [ ] `python3 scripts/validate.py _binaries/<name>.yaml` passes
- [ ] `command` blocks are copy-pasteable; use `ATTACKER`, `PORT`, `LHOST`, `LFILE` as placeholders
- [ ] OPSEC fields reflect real-world detection likelihood — be honest
- [ ] `difficulty` reflects how reliably the technique works across environments
- [ ] Referenced upstream entry linked in `references`

## Field Guidance

**difficulty**
- `low` — works in a default environment with no preconditions
- `medium` — requires a specific config, version, or multi-step setup
- `high` — fragile, version-specific, or requires a race condition

**opsec.noise**
- `low` — traffic/invocation blends with normal system activity
- `medium` — logged or flagged by some EDRs/SIEMs, not universal
- `high` — detected by most commercial EDRs out of the box

**opsec.artifacts** — list every log file, temp file, or audit event the technique creates.

## Style

- Technical, direct, no padding.
- `description` is one sentence. `notes` are one to two sentences max.
- Commands do not include comments. Comments go in `notes`.
- Do not add capabilities that don't directly apply.
