---
name: ffmpeg
capabilities:
- exec
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
- id: library-load
  description: Load an arbitrary shared library.
  capabilities:
  - exec
  command: |-
    ffmpeg -f lavfi -i anullsrc -af ladspa=file=/path/to/lib.so /path/to/temp-file.wav
    reset^J
references:
- https://gtfobins.github.io/gtfobins/ffmpeg/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
