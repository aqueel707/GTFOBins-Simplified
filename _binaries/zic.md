---
name: zic
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
    echo 'Rule Jordan 0 1 xxx Jan lastSun 2 1:00d -' >/path/to/temp-file
    echo 'Zone Test 2:00 Jordan CE%sT' >>/path/to/temp-file
    zic -d . -y /path/to/command /path/to/temp-file
  notes: |-
    This executes the command twice:

    - `/path/to/command 0 xxx`
    - `/path/to/command 1 xxx`

    Additionally the `Test` file is created.
references:
- https://gtfobins.github.io/gtfobins/zic/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
