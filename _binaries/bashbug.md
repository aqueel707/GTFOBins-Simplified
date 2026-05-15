---
name: bashbug
capabilities:
- exec
required_permissions:
  level: user
  notes: Inherits behavior from vi.
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  notes: Chains to vi; OPSEC follows that binary's profile.
persistence_potential: false
examples:
- id: inherit
  description: Inherits attack surface from `vi` — see that entry.
  capabilities:
  - exec
  command: bashbug
  notes: ''
references:
- https://gtfobins.github.io/gtfobins/bashbug/
tags:
- inherit
- vi
---
