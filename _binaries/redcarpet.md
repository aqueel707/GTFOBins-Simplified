---
name: redcarpet
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
  command: redcarpet /path/to/input-file
  notes: The file is actually parsed as a Markdown file.
references:
- https://gtfobins.github.io/gtfobins/redcarpet/
tags: []
---
