---
name: volatility
capabilities:
- exec
required_permissions:
  level: user
  notes: Inherits behavior from python.
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  notes: Chains to python; OPSEC follows that binary's profile.
persistence_potential: false
examples:
- id: inherit
  description: Inherits attack surface from `python` — see that entry.
  capabilities:
  - exec
  command: |-
    volatility -f /path/to/core-dump volshell
    ...
  notes: ''
references:
- https://gtfobins.github.io/gtfobins/volatility/
tags:
- inherit
- python
---
