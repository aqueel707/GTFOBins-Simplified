---
name: xelatex
capabilities:
- exec
required_permissions:
  level: user
  notes: Alias of `latex` — see that entry for details.
difficulty: low
opsec:
  noise: low
  artifacts: []
  notes: Identical behavior to `latex`.
persistence_potential: false
examples:
- id: alias
  description: This binary aliases to `latex`.
  capabilities:
  - exec
  command: '# See _binaries/latex.md for usage'
references:
- https://gtfobins.github.io/gtfobins/xelatex/
tags:
- alias
---
