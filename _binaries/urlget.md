---
name: urlget
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
  command: urlget - /path/to/input-file
  notes: This is part of `gettext` and usually not in `PATH`, e.g., on Arch it can be found at `/usr/lib/gettext/urlget`.
references:
- https://gtfobins.github.io/gtfobins/urlget/
tags: []
---
