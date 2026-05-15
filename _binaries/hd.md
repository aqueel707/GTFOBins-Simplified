---
name: hd
capabilities:
- exec
required_permissions:
  level: user
  notes: Alias of `hexdump` — see that entry for details.
difficulty: low
opsec:
  noise: low
  artifacts: []
  notes: Identical behavior to `hexdump`.
persistence_potential: false
examples:
- id: alias
  description: This binary aliases to `hexdump`.
  capabilities:
  - exec
  command: '# See _binaries/hexdump.md for usage'
references:
- https://gtfobins.github.io/gtfobins/hd/
tags:
- alias
---
