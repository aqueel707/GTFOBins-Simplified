---
name: tee
capabilities:
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
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: echo DATA | tee /path/to/output-file
  notes: Use `-a` to append data to exising files.
references:
- https://gtfobins.github.io/gtfobins/tee/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
