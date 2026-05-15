---
name: ntpdate
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
  command: ntpdate -a x -k /path/to/input-file -d localhost
  notes: The file is actually parsed and lines are leaked through error messages.
references:
- https://gtfobins.github.io/gtfobins/ntpdate/
tags: []
---
