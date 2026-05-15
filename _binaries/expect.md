---
name: expect
capabilities:
- exec
- spawn
- read
required_permissions:
  level: user
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  notes: ''
persistence_potential: true
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: expect /path/to/input-file
  notes: The file is read and parsed as an `expect` command file, the content of the first invalid line is returned in an error message.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: expect -c 'spawn /bin/sh -p;interact'
references:
- https://gtfobins.github.io/gtfobins/expect/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
