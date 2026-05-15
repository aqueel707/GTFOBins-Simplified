---
name: emacs
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
  notes: All the functions operate in the Emacs terminal interface.
persistence_potential: true
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: emacs /path/to/input-file
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    emacs /path/to/output-file
    DATA
    C-x C-s
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: emacs -Q -nw --eval '(term "/bin/sh")'
references:
- https://gtfobins.github.io/gtfobins/emacs/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
