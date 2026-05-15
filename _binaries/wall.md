---
name: wall
capabilities:
- read
required_permissions:
  level: sudo
  notes: Requires sudo rule for this binary.
difficulty: low
opsec:
  noise: low
  artifacts:
  - ~/.bash_history
  notes: ''
persistence_potential: false
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: wall --nobanner /path/to/input-file
  notes: The textual file is dumped on the current TTY (neither to `stdout` nor to `stderr`).
references:
- https://gtfobins.github.io/gtfobins/wall/
tags: []
---
