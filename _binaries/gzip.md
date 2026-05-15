---
name: gzip
capabilities:
- read
required_permissions:
  level: user
difficulty: low
opsec:
  noise: low
  artifacts:
  - ~/.bash_history
  notes: There are also a number of other utilities that rely on `gzip` under the hood, e.g., `zless`, `zcat`, `gunzip`, etc. Besides having similar features, they also allow privileged reads if `gzip` itself is SUID.
persistence_potential: false
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: gzip -c /path/to/input-file | gzip -d
references:
- https://gtfobins.github.io/gtfobins/gzip/
tags: []
---
