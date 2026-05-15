---
name: whiptail
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
  command: whiptail --textbox --scrolltext /path/to/input-file 0 0
  notes: The file is shown in an interactive TUI dialog made for displaying text, arrows can be used to scroll long content.
references:
- https://gtfobins.github.io/gtfobins/whiptail/
tags: []
---
