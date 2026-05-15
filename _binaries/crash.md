---
name: crash
capabilities:
- exec
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
- id: command
  description: Execute an arbitrary command.
  capabilities:
  - exec
  command: CRASHPAGER=/path/to/command crash -h
references:
- https://gtfobins.github.io/gtfobins/crash/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
