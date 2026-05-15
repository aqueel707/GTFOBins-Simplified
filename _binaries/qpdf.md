---
name: qpdf
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
  command: |-
    qpdf --empty --add-attachment /path/to/input-file --key=x -- /path/to/output-file
    qpdf --show-attachment=x /path/to/output-file
references:
- https://gtfobins.github.io/gtfobins/qpdf/
tags: []
---
