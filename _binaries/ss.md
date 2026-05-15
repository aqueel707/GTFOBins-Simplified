---
name: ss
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
  command: ss -a -F /path/to/input-file
  notes: The file content is actually parsed so only a part of the first line is returned as a part of an error message.
references:
- https://gtfobins.github.io/gtfobins/ss/
tags: []
---
