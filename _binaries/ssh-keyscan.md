---
name: ssh-keyscan
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
  command: ssh-keyscan -f /path/to/input-file
  notes: The file content is actually parsed so only a part of each line is returned as a part of an error message.
references:
- https://gtfobins.github.io/gtfobins/ssh-keyscan/
tags: []
---
