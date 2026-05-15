---
name: wc
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
  command: wc --files0-from /path/to/input-file
  notes: The file content is parsed as a sequence of `\x00` separated paths. On error the file content appears in a message.
references:
- https://gtfobins.github.io/gtfobins/wc/
tags: []
---
