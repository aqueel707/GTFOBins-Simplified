---
name: msgconv
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
  command: msgconv -P /path/to/input-file
  notes: The file is parsed and displayed as a Java `.properties` file.
references:
- https://gtfobins.github.io/gtfobins/msgconv/
tags: []
---
