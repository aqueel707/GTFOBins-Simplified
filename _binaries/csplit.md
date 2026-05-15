---
name: csplit
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
  command: |-
    csplit /path/to/input-file 1
    cat xx01
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    echo DATA >/path/to/temp-file
    csplit -z -b '%doutput-file' /path/to/temp-file 1
  notes: Writes the data to `xx0output-file` in the current working directory. If needed, a different prefix can be specified with `-f` (instead of `xx`).
references:
- https://gtfobins.github.io/gtfobins/csplit/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
