---
name: diff
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
  command: diff --line-format=%L /dev/null /path/to/input-file
- id: file-read-2
  description: Read an arbitrary file.
  capabilities:
  - read
  command: diff --recursive /path/to/empty-dir /path/to/input-dir/
  notes: This lists the content of a directory. `/path/to/empty-dir` can be any directory, but for convenience it is better to use an empty directory to avoid noise output.
references:
- https://gtfobins.github.io/gtfobins/diff/
tags: []
---
