---
name: fmt
capabilities:
- read
required_permissions:
  level: user
difficulty: medium
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
  command: fmt -pNON_EXISTING_PREFIX /path/to/input-file
- id: file-read-2
  description: Read an arbitrary file.
  capabilities:
  - read
  command: fmt -999 /path/to/input-file
  notes: This corrupts the output by wrapping very long lines at the given width (`999`).
references:
- https://gtfobins.github.io/gtfobins/fmt/
tags: []
---
