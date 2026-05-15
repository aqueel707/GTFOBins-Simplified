---
name: bc
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
    bc -s /path/to/input-file
    quit
  notes: The file content is actually parsed and appears as error messages.
references:
- https://gtfobins.github.io/gtfobins/bc/
tags: []
---
