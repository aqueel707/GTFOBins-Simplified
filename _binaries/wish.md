---
name: wish
capabilities:
- exec
required_permissions:
  level: user
  notes: Inherits behavior from tclsh.
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  notes: Chains to tclsh; OPSEC follows that binary's profile.
persistence_potential: false
examples:
- id: inherit
  description: Inherits attack surface from `tclsh` — see that entry.
  capabilities:
  - exec
  command: wish
  notes: ''
references:
- https://gtfobins.github.io/gtfobins/wish/
tags:
- inherit
- tclsh
---
