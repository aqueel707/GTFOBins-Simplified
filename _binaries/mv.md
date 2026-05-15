---
name: mv
capabilities:
- exec
- write
- suid
required_permissions:
  level: user
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  - File timestamps / inotify events on target paths
  notes: ''
persistence_potential: true
examples:
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    echo DATA >/path/to/temp-file
    mv /path/to/temp-file /path/to/output-file
- id: privilege-escalation
  description: Escalate to root via this binary.
  capabilities:
  - exec
  - suid
  command: mv /path/to/input-file /path/to/output-file
  notes: This can be used to move and then read or write files from a restricted file systems or with elevated privileges.
references:
- https://gtfobins.github.io/gtfobins/mv/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
