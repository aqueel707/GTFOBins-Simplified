---
name: asterisk
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
    asterisk -r
    !/bin/sh
  notes: A server instance must be already running, otherwise it can be started with `sudo asterisk -F`. Moreover, the invoking user must be able to access the socket.
references:
- https://gtfobins.github.io/gtfobins/asterisk/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
