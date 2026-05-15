---
name: check_log
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
  notes: This is the `check_log` Nagios plugin, available e.g. in `/usr/lib/nagios/plugins/`.
persistence_potential: true
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: check_log -F /path/to/input-file -O /dev/stdout
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: check_log -F /path/to/input-file -O /path/to/output-file
references:
- https://gtfobins.github.io/gtfobins/check_log/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
