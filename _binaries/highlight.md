---
name: highlight
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
  command: highlight --no-doc --failsafe /path/to/input-file
references:
- https://gtfobins.github.io/gtfobins/highlight/
tags: []
---
