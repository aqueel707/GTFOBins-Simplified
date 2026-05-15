---
name: nl
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
  command: nl -bn -w1 -s '' /path/to/input-file
  notes: The read file content is corrupted by a leading space added to each line.
references:
- https://gtfobins.github.io/gtfobins/nl/
tags: []
---
