---
name: apache2
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
  command: apache2 -f /path/to/input-file
  notes: The first line may be leaked as an error message.
- id: file-read-2
  description: Read an arbitrary file.
  capabilities:
  - read
  command: apache2 -C 'Define APACHE_RUN_DIR /' -C 'Include /path/to/input-file'
  notes: The first line may be leaked as an error message.
references:
- https://gtfobins.github.io/gtfobins/apache2/
tags: []
---
