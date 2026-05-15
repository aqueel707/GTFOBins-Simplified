---
name: mosquitto
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
  command: mosquitto -c /path/to/input-file
  notes: The file is actually parsed and the first wrong line (ending with a newline or a null character) is returned in an error message.
references:
- https://gtfobins.github.io/gtfobins/mosquitto/
tags: []
---
