---
name: red
capabilities:
- exec
required_permissions:
  level: user
  notes: Alias of `ed` — see that entry for details.
difficulty: low
opsec:
  noise: low
  artifacts: []
  notes: Identical behavior to `ed`.
persistence_potential: false
examples:
- id: alias
  description: This binary aliases to `ed`.
  capabilities:
  - exec
  command: '# See _binaries/ed.md for usage'
references:
- https://gtfobins.github.io/gtfobins/red/
tags:
- alias
---
