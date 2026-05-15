---
name: xetex
capabilities:
- exec
required_permissions:
  level: user
  notes: Alias of `tex` — see that entry for details.
difficulty: low
opsec:
  noise: low
  artifacts: []
  notes: Identical behavior to `tex`.
persistence_potential: false
examples:
- id: alias
  description: This binary aliases to `tex`.
  capabilities:
  - exec
  command: '# See _binaries/tex.md for usage'
references:
- https://gtfobins.github.io/gtfobins/xetex/
tags:
- alias
---
