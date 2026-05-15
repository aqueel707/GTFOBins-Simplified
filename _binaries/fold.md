---
name: fold
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
  command: fold -w999 /path/to/input-file
  notes: This corrupts the output by wrapping very long lines at the given width (`999`).
references:
- https://gtfobins.github.io/gtfobins/fold/
tags: []
---
