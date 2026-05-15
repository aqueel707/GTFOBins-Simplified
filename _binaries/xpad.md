---
name: xpad
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
  command: xpad -f /path/to/input-file
  notes: The file is displayed in a graphical window.
references:
- https://gtfobins.github.io/gtfobins/xpad/
tags: []
---
