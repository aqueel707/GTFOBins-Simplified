---
name: luatex
capabilities:
- exec
required_permissions:
  level: user
  notes: Inherits behavior from lua.
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  notes: Chains to lua; OPSEC follows that binary's profile.
persistence_potential: false
examples:
- id: inherit
  description: Inherits attack surface from `lua` — see that entry.
  capabilities:
  - exec
  command: luatex -shell-escape '\directlua{...}\end'
  notes: This allows to run Lua code (`...`).
references:
- https://gtfobins.github.io/gtfobins/luatex/
tags:
- inherit
- lua
---
