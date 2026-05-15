---
name: nft
capabilities:
- read
required_permissions:
  level: user
difficulty: medium
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
  command: nft -f /path/to/input-file
  notes: The content is actually parsed and corrupted by the command.
references:
- https://gtfobins.github.io/gtfobins/nft/
tags: []
---
