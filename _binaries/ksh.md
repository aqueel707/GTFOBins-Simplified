---
name: ksh
capabilities:
- exec
required_permissions:
  level: user
  notes: Alias of `bash` — see that entry for details.
difficulty: low
opsec:
  noise: low
  artifacts: []
  notes: Identical behavior to `bash`.
persistence_potential: false
examples:
- id: alias
  description: This binary aliases to `bash`.
  capabilities:
  - exec
  command: '# See _binaries/bash.md for usage'
references:
- https://gtfobins.github.io/gtfobins/ksh/
tags:
- alias
---
