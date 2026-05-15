---
name: apt
capabilities:
- exec
required_permissions:
  level: user
  notes: Alias of `apt-get` — see that entry for details.
difficulty: low
opsec:
  noise: low
  artifacts: []
  notes: Identical behavior to `apt-get`.
persistence_potential: false
examples:
- id: alias
  description: This binary aliases to `apt-get`.
  capabilities:
  - exec
  command: '# See _binaries/apt-get.md for usage'
references:
- https://gtfobins.github.io/gtfobins/apt/
tags:
- alias
---
