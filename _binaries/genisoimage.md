---
name: genisoimage
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
  command: genisoimage -q -o - /path/to/input-file
  notes: The output is placed inside the ISO9660 file system binary format, it can be mounted or extracted with tools like `7z`.
- id: file-read-2
  description: Read an arbitrary file.
  capabilities:
  - read
  command: genisoimage -sort /path/to/input-file
  notes: The file is parsed, and some of its content is disclosed by the error messages.
references:
- https://gtfobins.github.io/gtfobins/genisoimage/
tags: []
---
