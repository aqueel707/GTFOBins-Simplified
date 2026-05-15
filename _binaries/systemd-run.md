---
name: systemd-run
capabilities:
- exec
- spawn
required_permissions:
  level: sudo
  notes: Requires sudo rule for this binary.
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
  command: systemd-run /path/to/command
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: systemd-run -S
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: systemd-run -t /bin/sh
references:
- https://gtfobins.github.io/gtfobins/systemd-run/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
