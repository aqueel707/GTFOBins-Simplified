---
name: basez
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
  command: basez /path/to/input-file | basez --decode
references:
- https://gtfobins.github.io/gtfobins/basez/
tags: []
---
