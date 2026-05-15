---
name: basenc
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
  command: basenc --base64 /path/to/input-file | basenc -d --base64
references:
- https://gtfobins.github.io/gtfobins/basenc/
tags: []
---
