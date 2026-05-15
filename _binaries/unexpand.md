---
name: unexpand
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
  command: unexpand -t999 /path/to/input-file
  notes: Convert sequences of (e.g., `999`) spaces to tab.
references:
- https://gtfobins.github.io/gtfobins/unexpand/
tags: []
---
