---
name: awk
capabilities:
- exec
required_permissions:
  level: user
  notes: Alias of `mawk` — see that entry for details.
difficulty: low
opsec:
  noise: low
  artifacts: []
  notes: Identical behavior to `mawk`.
persistence_potential: false
examples:
- id: alias
  description: This binary aliases to `mawk`.
  capabilities:
  - exec
  command: '# See _binaries/mawk.md for usage'
references:
- https://gtfobins.github.io/gtfobins/awk/
tags:
- alias
---
