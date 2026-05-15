---
name: rustfmt
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
  command: rustfmt /path/to/input-file
  notes: Partial content is displayed as error messages.
references:
- https://gtfobins.github.io/gtfobins/rustfmt/
tags: []
---
