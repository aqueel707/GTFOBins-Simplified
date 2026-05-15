---
name: rev
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
  command: rev /path/to/input-file | rev
references:
- https://gtfobins.github.io/gtfobins/rev/
tags: []
---
