---
name: dstat
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
  command: dstat --xxx
  notes: |-
    `dstat` allows you to run arbitrary Python scripts loaded as "external plugins" if they are located in one of the directories, stated in the `dstat` man page under "FILES":

    - `~/.dstat/`
    - `(path of binary)/plugins/`
    - `/usr/share/dstat/`
    - `/usr/local/share/dstat/`

    Pick the one that you can write into. The plugin named `xxx` file name must be defined in the `dstat_xxx.py` file.
references:
- https://gtfobins.github.io/gtfobins/dstat/
tags:
- inherit
- python
---
