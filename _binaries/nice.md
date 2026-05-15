---
name: nice
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
  command: nice /bin/sh -p
references:
- https://gtfobins.github.io/gtfobins/nice/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
