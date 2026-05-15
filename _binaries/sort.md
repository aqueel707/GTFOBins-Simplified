---
name: sort
capabilities:
- read
- write
required_permissions:
  level: user
difficulty: low
opsec:
  noise: low
  artifacts:
  - ~/.bash_history
  - File timestamps / inotify events on target paths
  notes: ''
persistence_potential: true
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: sort -m /path/to/input-file
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: echo DATA | sort -m -o /path/to/output-file
references:
- https://gtfobins.github.io/gtfobins/sort/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
