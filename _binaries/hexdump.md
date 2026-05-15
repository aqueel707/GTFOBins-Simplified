---
name: hexdump
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
  command: hd /path/to/input-file
  notes: The output is actually an hex dump.
references:
- https://gtfobins.github.io/gtfobins/hexdump/
tags: []
---
