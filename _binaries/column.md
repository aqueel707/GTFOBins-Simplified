---
name: column
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
  command: column /path/to/input-file
  notes: This program expects textual data.
references:
- https://gtfobins.github.io/gtfobins/column/
tags: []
---
