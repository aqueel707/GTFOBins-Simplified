---
name: nawk
capabilities:
- exec
required_permissions:
  level: user
  notes: Alias of `gawk` — see that entry for details.
difficulty: low
opsec:
  noise: low
  artifacts: []
  notes: Identical behavior to `gawk`.
persistence_potential: false
examples:
- id: alias
  description: This binary aliases to `gawk`.
  capabilities:
  - exec
  command: '# See _binaries/gawk.md for usage'
references:
- https://gtfobins.github.io/gtfobins/nawk/
tags:
- alias
---
