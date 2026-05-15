---
name: links
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
  command: links /path/to/input-file
  notes: The result is displayed in a TUI interface.
references:
- https://gtfobins.github.io/gtfobins/links/
tags: []
---
