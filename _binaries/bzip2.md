---
name: bzip2
capabilities:
- read
required_permissions:
  level: user
difficulty: low
opsec:
  noise: low
  artifacts:
  - ~/.bash_history
  notes: There are also a number of other utilities that rely on `bzip2` under the hood, e.g., `bzless`, `bzcat`, `bunzip2`, etc. Besides having similar features, they also allow privileged reads if `bzip2` itself is SUID.
persistence_potential: false
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: bzip2 -c /path/to/input-file | bzip2 -d
references:
- https://gtfobins.github.io/gtfobins/bzip2/
tags: []
---
