---
name: screen
capabilities:
- exec
- spawn
- write
required_permissions:
  level: user
difficulty: medium
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
  command: screen -L -Logfile /path/to/output-file echo DATA
  notes: Data is appended to the file and `\n` is converted to `\r\n`.
- id: file-write-2
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: screen -L /path/to/output-file echo DATA
  notes: Data is appended to the file and `\n` is converted to `\r\n`.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: screen
references:
- https://gtfobins.github.io/gtfobins/screen/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
