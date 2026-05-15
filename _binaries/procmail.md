---
name: procmail
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
  command: |-
    echo -e ':0\n| /path/to/command >/path/to/temp-file
    procmail -m /path/to/temp-file
  notes: The program is picky about the file ownership, and waits for some input.
references:
- https://gtfobins.github.io/gtfobins/procmail/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
