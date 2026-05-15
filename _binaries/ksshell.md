---
name: ksshell
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
  command: ksshell -i /path/to/input-file
  notes: Each line is corrupted by a prefix string. Also consider that lines are actually parsed as `kickstart` scripts thus some file contents may lead to unexpected results.
references:
- https://gtfobins.github.io/gtfobins/ksshell/
tags: []
---
