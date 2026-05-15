---
name: strace
capabilities:
- exec
- spawn
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
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: strace -s 999 -o /path/to/output-file strace - DATA
  notes: The data to be written appears amid the syscall log, quoted and with special characters escaped in octal notation. The string representation will be truncated, pick a value big enough instead of `999`. More generally, any binary that executes whatever syscall passing arbitrary data can be used in place of `strace - DATA`.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: strace -o /dev/null /bin/sh -p
references:
- https://gtfobins.github.io/gtfobins/strace/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
