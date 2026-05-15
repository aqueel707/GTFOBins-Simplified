---
name: pdb
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
    echo '...' >/path/to/temp-file
    pdb /path/to/temp-file
    cont
  notes: This allows to run Python code (`...`).
references:
- https://gtfobins.github.io/gtfobins/pdb/
tags:
- inherit
- python
---
