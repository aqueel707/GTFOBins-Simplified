---
name: od
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
  command: od -An -c -w999 /path/to/input-file
  notes: Three spaces are added before each character in the read file (wrapped at the specified value, i.e., `999`), and non-printable chars are printed as backslash escape sequences.
references:
- https://gtfobins.github.io/gtfobins/od/
tags: []
---
