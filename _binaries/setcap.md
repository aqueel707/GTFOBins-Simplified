---
name: setcap
capabilities:
- exec
- suid
required_permissions:
  level: suid
  notes: Requires SUID bit set on the binary.
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
  command: setcap cap_setuid+ep /path/to/command
  notes: This can be used to assign capabilities to executable files.
references:
- https://gtfobins.github.io/gtfobins/setcap/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
