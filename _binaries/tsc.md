---
name: tsc
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
  command: tsc /path/to/input-file.ts
  notes: Content is leaked as error messages. The file extension must be one of the supported ones, e.g., `.ts`, `.tsx`, etc.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: tsc /path/to/input-file.ts --outFile /path/to/output-file
  notes: Content is leaked as error messages and written to file. The file extension must be one of the supported ones, e.g., `.ts`, `.tsx`, etc.
references:
- https://gtfobins.github.io/gtfobins/tsc/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
