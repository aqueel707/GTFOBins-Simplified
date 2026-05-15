---
name: at
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
- id: command
  description: Execute an arbitrary command.
  capabilities:
  - exec
  command: echo /path/to/command | at now
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: echo "/bin/sh <$(tty) >$(tty) 2>$(tty)" | at now; tail -f /dev/null
  notes: '`tail` is used to pause the terminal.'
references:
- https://gtfobins.github.io/gtfobins/at/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
