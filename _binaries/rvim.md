---
name: rvim
capabilities:
- exec
required_permissions:
  level: user
  notes: Alias of `vim` — see that entry for details.
difficulty: low
opsec:
  noise: low
  artifacts: []
  notes: Identical behavior to `vim`.
persistence_potential: false
examples:
- id: alias
  description: This binary aliases to `vim`.
  capabilities:
  - exec
  command: '# See _binaries/vim.md for usage'
references:
- https://gtfobins.github.io/gtfobins/rvim/
tags:
- alias
---
