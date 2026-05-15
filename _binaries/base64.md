---
name: base64
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
  command: base64 /path/to/input-file | base64 --decode
references:
- https://gtfobins.github.io/gtfobins/base64/
tags: []
---
