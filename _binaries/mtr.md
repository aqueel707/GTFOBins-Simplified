---
name: mtr
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
  command: mtr --raw -F /path/to/input-file
  notes: The file is actually parsed, thus the content is corrupted by error prints.
references:
- https://gtfobins.github.io/gtfobins/mtr/
tags: []
---
