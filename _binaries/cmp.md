---
name: cmp
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
  command: cmp /path/to/input-file /dev/zero -b -l
  notes: Dump the bytes of the input file that are different from the NUL byte in a tabular format.
references:
- https://gtfobins.github.io/gtfobins/cmp/
tags: []
---
