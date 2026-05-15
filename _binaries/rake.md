---
name: rake
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
  command: rake -f /path/to/input-file
  notes: The file is actually parsed and the first wrong line is returned in an error message.
references:
- https://gtfobins.github.io/gtfobins/rake/
tags: []
---
