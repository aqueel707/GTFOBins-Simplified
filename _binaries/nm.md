---
name: nm
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
  command: nm /path/to/input-file
  notes: The file content is treated as command line options and disclosed through error messages.
references:
- https://gtfobins.github.io/gtfobins/nm/
tags: []
---
