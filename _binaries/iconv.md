---
name: iconv
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
  notes: The `8859_1` encoding is used as it accepts any single-byte sequence, thus it allows to read/write arbitrary files. Other encoding combinations may corrupt the result.
persistence_potential: true
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: iconv -f 8859_1 -t 8859_1 /path/to/input-file
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: echo DATA | iconv -f 8859_1 -t 8859_1 -o /path/to/output-file
references:
- https://gtfobins.github.io/gtfobins/iconv/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
