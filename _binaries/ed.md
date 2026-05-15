---
name: ed
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
  command: |-
    ed /path/to/input-file
    ,p
    q
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    ed /path/to/output-file
    a
    DATA
    .
    w
    q
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    ed
    !/bin/sh
    q
references:
- https://gtfobins.github.io/gtfobins/ed/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
