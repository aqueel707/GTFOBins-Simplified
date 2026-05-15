---
name: gimp
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
  command: gimp -idf --batch-interpreter=python-fu-eval -b '...'
  notes: This allows to run Python code (`...`). It hangs afterwards and can be terminated by pressing `Ctrl-C`.
references:
- https://gtfobins.github.io/gtfobins/gimp/
tags:
- inherit
- python
---
