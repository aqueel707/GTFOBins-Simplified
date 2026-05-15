---
name: yelp
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
  command: yelp man:/path/to/input-file
  notes: This spawns a graphical window containing the file content somehow corrupted by word wrapping.
references:
- https://gtfobins.github.io/gtfobins/yelp/
tags: []
---
