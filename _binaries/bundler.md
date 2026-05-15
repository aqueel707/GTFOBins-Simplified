---
name: bundler
capabilities:
- exec
required_permissions:
  level: user
  notes: Alias of `bundle` — see that entry for details.
difficulty: low
opsec:
  noise: low
  artifacts: []
  notes: Identical behavior to `bundle`.
persistence_potential: false
examples:
- id: alias
  description: This binary aliases to `bundle`.
  capabilities:
  - exec
  command: '# See _binaries/bundle.md for usage'
references:
- https://gtfobins.github.io/gtfobins/bundler/
tags:
- alias
---
