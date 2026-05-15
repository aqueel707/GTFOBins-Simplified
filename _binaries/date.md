---
name: date
capabilities:
- read
required_permissions:
  level: user
difficulty: medium
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
  command: date -f /path/to/input-file
  notes: Each line is corrupted by a prefix string and wrapped inside quotes.
references:
- https://gtfobins.github.io/gtfobins/date/
tags: []
---
