---
name: base58
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
  command: base58 /path/to/input-file | base58 --decode
references:
- https://gtfobins.github.io/gtfobins/base58/
tags: []
---
