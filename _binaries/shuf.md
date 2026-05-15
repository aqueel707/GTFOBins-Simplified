---
name: shuf
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
  command: shuf -z /path/to/input-file
  notes: The read file content is corrupted by randomizing the order of NUL terminated strings.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: shuf -e DATA -o /path/to/output-file
  notes: The written file content is corrupted by adding a newline.
references:
- https://gtfobins.github.io/gtfobins/shuf/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
