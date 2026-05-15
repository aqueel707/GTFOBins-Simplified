---
name: dig
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
  command: dig -f /path/to/input-file
  notes: Each input line is treated as a lookup query for the `dig` command and the output is corrupted with the result or errors of the operation.
references:
- https://gtfobins.github.io/gtfobins/dig/
tags: []
---
