---
name: atobm
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
  command: atobm /path/to/input-file
  notes: Outputs only the first line of the file to standard error without the `-` and `#` characters, this can be customized with the `-c` option, by default is `-c -#`. Content can be retrieved with `awk -F "'" '{printf "%s", $2}'`.
references:
- https://gtfobins.github.io/gtfobins/atobm/
tags: []
---
