---
name: efax
capabilities:
- read
required_permissions:
  level: suid
  notes: Requires SUID bit set on the binary.
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
  command: efax -d /path/to/input-file
  notes: The content is actually parsed by the command.
references:
- https://gtfobins.github.io/gtfobins/efax/
tags: []
---
