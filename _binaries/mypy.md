---
name: mypy
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
  command: mypy /path/to/input-file
  notes: Partial content is leaked as error messages.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: mypy /path/to/input-file --junit-xml /path/to/output-file
  notes: Partial content is leaked as error messages inside some XML tags.
references:
- https://gtfobins.github.io/gtfobins/mypy/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
