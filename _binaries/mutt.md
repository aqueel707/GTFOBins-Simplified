---
name: mutt
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
  command: mutt -F /path/to/input-file
  notes: The file is leaked as error messages.
references:
- https://gtfobins.github.io/gtfobins/mutt/
tags: []
---
