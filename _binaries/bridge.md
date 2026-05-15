---
name: bridge
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
  command: bridge -b /path/to/input-file
  notes: Outputs the first line of the file (until the first whitespace) inside an error message to stdandard error.
references:
- https://gtfobins.github.io/gtfobins/bridge/
tags: []
---
