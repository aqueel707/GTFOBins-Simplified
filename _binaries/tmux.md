---
name: tmux
capabilities:
- exec
- spawn
- read
required_permissions:
  level: user
difficulty: medium
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  notes: ''
persistence_potential: true
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: tmux -f /path/to/input-file
  notes: The file is read and parsed as a `tmux` configuration file, part of the first invalid line is returned in an error message.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: tmux -c /bin/sh
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: tmux -S /path/to/socket
  notes: Provided to have enough permissions to access the socket (e.g., `/tmp/tmux-xxx/default`).
references:
- https://gtfobins.github.io/gtfobins/tmux/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
