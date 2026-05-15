---
name: xmore
capabilities:
- read
required_permissions:
  level: user
difficulty: low
opsec:
  noise: low
  artifacts:
  - ~/.bash_history
  notes: This requires a running X server.
persistence_potential: false
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: xmore /path/to/input-file
  notes: The file is displayed in a graphical window.
references:
- https://gtfobins.github.io/gtfobins/xmore/
tags: []
---
