---
name: systemd-resolve
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
  command: systemd-resolve --status
  notes: ''
references:
- https://gtfobins.github.io/gtfobins/systemd-resolve/
tags:
- inherit
- less
---
