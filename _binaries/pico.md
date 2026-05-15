---
name: pico
capabilities:
- exec
required_permissions:
  level: user
  notes: Alias of `nano` — see that entry for details.
difficulty: low
opsec:
  noise: low
  artifacts: []
  notes: Identical behavior to `nano`.
persistence_potential: false
examples:
- id: alias
  description: This binary aliases to `nano`.
  capabilities:
  - exec
  command: '# See _binaries/nano.md for usage'
references:
- https://gtfobins.github.io/gtfobins/pico/
tags:
- alias
---
