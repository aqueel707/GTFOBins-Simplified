---
name: aspell
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
  command: aspell -c /path/to/input-file
  notes: The textual file is displayed in an interactive TUI showing only the parts that contain mispelled words.
- id: file-read-2
  description: Read an arbitrary file.
  capabilities:
  - read
  command: aspell --conf /path/to/input-file
  notes: The first word is likely displayed as error messaged, and converted to lowercase.
references:
- https://gtfobins.github.io/gtfobins/aspell/
tags: []
---
