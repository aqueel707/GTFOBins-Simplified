---
name: time
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
  command: time /bin/sh -p
  notes: Note that the shell might have its own builtin `time` implementation, which may behave differently than the binary, which is often located at `/usr/bin/time`.
references:
- https://gtfobins.github.io/gtfobins/time/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
