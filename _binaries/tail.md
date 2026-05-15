---
name: tail
capabilities:
- read
required_permissions:
  level: user
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
  command: tail -c+0 /path/to/input-file
references:
- https://gtfobins.github.io/gtfobins/tail/
tags: []
---
