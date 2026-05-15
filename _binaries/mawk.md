---
name: mawk
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
  command: mawk '//' /path/to/input-file
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: mawk 'BEGIN { print "DATA" > "/path/to/output-file" }'
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: mawk 'BEGIN {system("/bin/sh")}'
references:
- https://gtfobins.github.io/gtfobins/mawk/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
