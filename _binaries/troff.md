---
name: troff
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
  command: troff /path/to/input-file
  notes: The file is typeset but text is still readable in the output, alternatively the output can be read with `man -l`.
references:
- https://gtfobins.github.io/gtfobins/troff/
tags: []
---
