---
name: uniq
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
  command: uniq /path/to/input-file
  notes: The read file content is corrupted by squashing multiple adjacent lines.
references:
- https://gtfobins.github.io/gtfobins/uniq/
tags: []
---
