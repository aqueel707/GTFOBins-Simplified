---
name: tbl
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
  command: tbl /path/to/input-file
  notes: The read file content is corrupted by additional text at the beginning.
references:
- https://gtfobins.github.io/gtfobins/tbl/
tags: []
---
