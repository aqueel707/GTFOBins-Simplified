---
name: pyright
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
  command: pyright /path/to/input-file
  notes: Content is leaked as error messages.
- id: file-read-2
  description: Read an arbitrary file.
  capabilities:
  - read
  command: pyright --outputjson /path/to/input-file
  notes: Content is leaked as error messages in JSON format.
- id: file-read-3
  description: Read an arbitrary file.
  capabilities:
  - read
  command: pyright -w /path/to/input-dir/
  notes: Recursively walks directories, parsing all Python files and leaking some contents through diagnostics.
references:
- https://gtfobins.github.io/gtfobins/pyright/
tags: []
---
