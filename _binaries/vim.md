---
name: vim
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
  command: vim -c ':redir! >/path/to/output-file | echo "DATA" | redir END | q'
references:
- https://gtfobins.github.io/gtfobins/vim/
tags: []
---
