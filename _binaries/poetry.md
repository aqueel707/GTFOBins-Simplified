---
name: poetry
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
    poetry run python /path/to/temp-file
  notes: |-
    This allows to run Python code (`...`).

    A valid `pyproject.toml` file must be present in the current working directory, you can create one with `poetry init -n`.
references:
- https://gtfobins.github.io/gtfobins/poetry/
tags:
- inherit
- python
---
