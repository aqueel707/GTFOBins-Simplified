---
name: soelim
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
  command: soelim /path/to/input-file
  notes: The content is actually parsed and corrupted by the command.
references:
- https://gtfobins.github.io/gtfobins/soelim/
tags: []
---
