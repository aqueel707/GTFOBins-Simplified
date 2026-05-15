---
name: alpine
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
  command: alpine -F /path/to/input-file
  notes: The file is displayed in the terminal interface. Other options might be available, for example, by pressing `S` is possible to save the file content elsewhere.
references:
- https://gtfobins.github.io/gtfobins/alpine/
tags: []
---
