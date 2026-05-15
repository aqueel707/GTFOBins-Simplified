---
name: strings
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
  command: strings /path/to/input-file
  notes: This only returns ASCII strings.
references:
- https://gtfobins.github.io/gtfobins/strings/
tags: []
---
