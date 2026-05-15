---
name: tic
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
  command: tic -C /path/to/input-file
  notes: This translates a terminfo file from source format into compiled format. It will attempt to translate an arbitrary file and output the contents of the file on failure.
references:
- https://gtfobins.github.io/gtfobins/tic/
tags: []
---
