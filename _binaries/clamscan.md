---
name: clamscan
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
    touch x.yara
    clamscan --no-summary -d x.yara -f /path/to/input-file 2>&1 | sed -nE 's/^(.*): No such file or directory$/\1/p'
  notes: Each line of the file is interpreted as a path and the content is leaked via error messages. The output can optionally be cleaned using `sed`.
references:
- https://gtfobins.github.io/gtfobins/clamscan/
tags: []
---
