---
name: arp
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
  command: arp -v -f /path/to/input-file
  notes: Lines are likely leaked as error messages.
references:
- https://gtfobins.github.io/gtfobins/arp/
tags: []
---
