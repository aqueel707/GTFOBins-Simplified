---
name: ssh-keygen
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
- id: library-load
  description: Load an arbitrary shared library.
  capabilities:
  - exec
  command: ssh-keygen -D /path/to/lib.so
  notes: The shared library must contain the `void C_GetFunctionList() {}` function.
references:
- https://gtfobins.github.io/gtfobins/ssh-keygen/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
