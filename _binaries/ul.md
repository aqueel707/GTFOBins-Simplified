---
name: ul
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
  command: ul /path/to/input-file
  notes: The read file content is corrupted by replacing occurrences of `$'\b_'` to terminal sequences and by converting tabs to spaces.
references:
- https://gtfobins.github.io/gtfobins/ul/
tags: []
---
