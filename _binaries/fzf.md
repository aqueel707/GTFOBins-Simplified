---
name: fzf
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
  command: fzf --listen=12345
  notes: |-
    Commands can be issued via POST requests, for example:

    ```
    curl http://localhost:12345 -d 'execute(/path/to/command)'
    ```
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: fzf --bind 'enter:execute(/bin/sh)'
  notes: Press `Enter` to receive the shell.
references:
- https://gtfobins.github.io/gtfobins/fzf/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
