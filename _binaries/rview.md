---
name: rview
capabilities:
- exec
required_permissions:
  level: user
  notes: Alias of `view` — see that entry for details.
difficulty: low
opsec:
  noise: low
  artifacts: []
  notes: Identical behavior to `view`.
persistence_potential: false
examples:
- id: alias
  description: This binary aliases to `view`.
  capabilities:
  - exec
  command: '# See _binaries/view.md for usage'
references:
- https://gtfobins.github.io/gtfobins/rview/
tags:
- alias
---
