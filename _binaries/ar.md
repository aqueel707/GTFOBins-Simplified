---
name: ar
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
  command: |-
    ar r /path/to/output-file /path/to/input-file
    ar p /path/to/output-file
references:
- https://gtfobins.github.io/gtfobins/ar/
tags: []
---
