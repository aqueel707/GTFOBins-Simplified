---
name: comm
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
  command: comm /path/to/input-file /dev/null
  notes: A newline is appended to the file.
references:
- https://gtfobins.github.io/gtfobins/comm/
tags: []
---
