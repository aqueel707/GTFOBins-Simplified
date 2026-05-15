---
name: xdg-user-dir
capabilities:
- exec
- spawn
required_permissions:
  level: user
difficulty: medium
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  notes: The current implementation of `xdg-user-dir` is basically `eval echo \${XDG_${1}_DIR:-$HOME}`, thus is can be easily used to achieve command execution.
persistence_potential: true
examples:
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: 'xdg-user-dir ''}; /bin/sh #'''
references:
- https://gtfobins.github.io/gtfobins/xdg-user-dir/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
