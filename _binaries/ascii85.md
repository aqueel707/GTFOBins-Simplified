---
name: ascii85
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
  command: ascii85 /path/to/input-file | ascii85 --decode
references:
- https://gtfobins.github.io/gtfobins/ascii85/
tags: []
---
