---
name: sqlite3
capabilities:
- exec
- spawn
- read
- write
required_permissions:
  level: user
difficulty: low
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
    sqlite3 <<EOF
    CREATE TABLE x(x TEXT);
    .import /path/to/input-file x
    SELECT * FROM x;
    EOF
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: sqlite3 /dev/null -cmd '.output /path/to/output-file' 'select "DATA";'
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: sqlite3 /dev/null '.shell /bin/sh'
references:
- https://gtfobins.github.io/gtfobins/sqlite3/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
