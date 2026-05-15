---
name: pax
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
  command: pax -w /path/to/input-file | tar -xO
references:
- https://gtfobins.github.io/gtfobins/pax/
tags: []
---
