---
name: fping
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
  command: fping -f /path/to/input-file
  notes: Each line is treated as an hostname and it's leaked as an error message.
references:
- https://gtfobins.github.io/gtfobins/fping/
tags: []
---
