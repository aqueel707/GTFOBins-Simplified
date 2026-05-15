---
name: gem
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
  command: gem open -e '/bin/sh -s' debug
  notes: This requires the name of an installed gem to be provided, e.g., `debug` is usually installed.
references:
- https://gtfobins.github.io/gtfobins/gem/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
