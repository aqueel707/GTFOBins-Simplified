---
name: arj
capabilities:
- read
- write
required_permissions:
  level: user
difficulty: low
opsec:
  noise: low
  artifacts:
  - ~/.bash_history
  - File timestamps / inotify events on target paths
  notes: ''
persistence_potential: true
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: |-
    arj a /path/to/output-file /path/to/input-file
    arj p /path/to/output-file
  notes: The `.arj` suffix will be added to `output-file`.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    echo DATA >output-file
    arj a x output-file
    arj e x /path/to/output-dir/
  notes: The `.arj` suffix will be added to `x`.
references:
- https://gtfobins.github.io/gtfobins/arj/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
