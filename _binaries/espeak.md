---
name: espeak
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
  command: espeak -qXf /path/to/input-file
  notes: The file content appears in the middle of other textual information as phonemes.
references:
- https://gtfobins.github.io/gtfobins/espeak/
tags: []
---
