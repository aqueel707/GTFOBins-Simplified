---
name: lastb
capabilities:
- exec
required_permissions:
  level: user
  notes: Alias of `last` — see that entry for details.
difficulty: low
opsec:
  noise: low
  artifacts: []
  notes: Identical behavior to `last`.
persistence_potential: false
examples:
- id: alias
  description: This binary aliases to `last`.
  capabilities:
  - exec
  command: '# See _binaries/last.md for usage'
references:
- https://gtfobins.github.io/gtfobins/lastb/
tags:
- alias
---
