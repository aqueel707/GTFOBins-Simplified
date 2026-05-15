---
name: tac
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
  command: tac -s 'RANDOM' /path/to/input-file
  notes: Make sure that `RANDOM` does not appear into the file to read otherwise the content of the file is corrupted by reversing the order of `RANDOM`-separated chunks.
references:
- https://gtfobins.github.io/gtfobins/tac/
tags: []
---
