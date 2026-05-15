---
name: dash
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
  command: dash -c 'echo DATA >/path/to/output-file'
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: dash
references:
- https://gtfobins.github.io/gtfobins/dash/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
