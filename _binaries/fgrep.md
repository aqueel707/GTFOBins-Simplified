---
name: fgrep
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
  command: grep '' /path/to/input-file
references:
- https://gtfobins.github.io/gtfobins/fgrep/
tags: []
---
