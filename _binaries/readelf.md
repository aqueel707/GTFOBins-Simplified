---
name: readelf
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
  command: readelf -a @/path/to/input-file
  notes: Each line is corrupted by a prefix string and wrapped inside single quotes. Also consider that lines are actually parsed as `readelf` options thus some file contents may lead to unexpected results.
references:
- https://gtfobins.github.io/gtfobins/readelf/
tags: []
---
