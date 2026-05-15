---
name: w3m
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
  command: w3m -dump /path/to/input-file
references:
- https://gtfobins.github.io/gtfobins/w3m/
tags: []
---
