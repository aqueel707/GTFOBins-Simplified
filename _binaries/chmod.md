---
name: chmod
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
  command: chmod 6777 /path/to/input-file
  notes: This can be run with elevated privileges to change permissions (`6` denotes the SUID bits) and then read, write, or execute a file.
references:
- https://gtfobins.github.io/gtfobins/chmod/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
