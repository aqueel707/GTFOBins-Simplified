---
name: dialog
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
  command: dialog --textbox /path/to/input-file 0 0
  notes: The file is shown in an interactive TUI dialog.
references:
- https://gtfobins.github.io/gtfobins/dialog/
tags: []
---
