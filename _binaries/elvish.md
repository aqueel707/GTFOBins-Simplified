---
name: elvish
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
  command: elvish -c 'print (slurp </path/to/input-file)'
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: elvish -c 'print DATA >/path/to/output-file'
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: elvish
references:
- https://gtfobins.github.io/gtfobins/elvish/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
