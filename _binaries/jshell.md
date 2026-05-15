---
name: jshell
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
  command: |-
    jshell
    jshell> /open /path/to/input-file
  notes: The content is leaked as error messages.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    jshell
    String x = "DATA";
    /save /path/to/output-file
  notes: Writes only the valid Java code to file.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    jshell
    Runtime.getRuntime().exec("/path/to/command");
references:
- https://gtfobins.github.io/gtfobins/jshell/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
