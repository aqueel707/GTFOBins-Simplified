---
name: cargo
capabilities:
- exec
required_permissions:
  level: user
  notes: Inherits behavior from less.
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  notes: Chains to less; OPSEC follows that binary's profile.
persistence_potential: false
examples:
- id: inherit
  description: Inherits attack surface from `less` — see that entry.
  capabilities:
  - exec
  command: cargo help doc
  notes: ''
references:
- https://gtfobins.github.io/gtfobins/cargo/
tags:
- inherit
- less
---
