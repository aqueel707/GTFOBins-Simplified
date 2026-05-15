---
name: apache2ctl
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
  command: apache2ctl -c 'Include /path/to/input-file'
  notes: The first line only is likely leaked as an error message.
references:
- https://gtfobins.github.io/gtfobins/apache2ctl/
tags: []
---
