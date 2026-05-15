---
name: eb
capabilities:
- exec
required_permissions:
  level: user
  notes: Inherits behavior from journalctl.
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  notes: Chains to journalctl; OPSEC follows that binary's profile.
persistence_potential: false
examples:
- id: inherit
  description: Inherits attack surface from `journalctl` — see that entry.
  capabilities:
  - exec
  command: eb logs
  notes: ''
references:
- https://gtfobins.github.io/gtfobins/eb/
tags:
- inherit
- journalctl
---
