---
name: ascii-xfr
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
  command: ascii-xfr -ns /path/to/input-file
references:
- https://gtfobins.github.io/gtfobins/ascii-xfr/
tags: []
---
