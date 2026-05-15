---
name: ptx
capabilities:
- read
required_permissions:
  level: user
difficulty: low
opsec:
  noise: low
  artifacts:
  - ~/.bash_history
  notes: While the program is capable of reading the file, it outputs a "permuted index" of its content, thus altering it. Adjusting the options could yield more readable outputs.
persistence_potential: false
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: ptx -w 999 /path/to/input-file
references:
- https://gtfobins.github.io/gtfobins/ptx/
tags: []
---
