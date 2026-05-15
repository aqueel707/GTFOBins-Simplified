---
name: bbot
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
  command: bbot -d -cy /path/to/input-file
  notes: The file is displayed in the debug log.
references:
- https://gtfobins.github.io/gtfobins/bbot/
tags: []
---
