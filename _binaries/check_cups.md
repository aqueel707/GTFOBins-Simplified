---
name: check_cups
capabilities:
- read
required_permissions:
  level: user
difficulty: low
opsec:
  noise: low
  artifacts:
  - ~/.bash_history
  notes: This is the `check_cups` Nagios plugin, available e.g. in `/usr/lib/nagios/plugins/`.
persistence_potential: false
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: check_cups --extra-opts=@/path/to/input-file
  notes: The read file content is limited to the first line.
references:
- https://gtfobins.github.io/gtfobins/check_cups/
tags: []
---
