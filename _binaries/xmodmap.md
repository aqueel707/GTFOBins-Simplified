---
name: xmodmap
capabilities:
- read
required_permissions:
  level: user
difficulty: low
opsec:
  noise: low
  artifacts:
  - ~/.bash_history
  notes: This requires a running X server.
persistence_potential: false
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: xmodmap -v /path/to/input-file
  notes: The read file content is corrupted by error prints.
references:
- https://gtfobins.github.io/gtfobins/xmodmap/
tags: []
---
