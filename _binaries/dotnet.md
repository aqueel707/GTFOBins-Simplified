---
name: dotnet
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
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: |-
    dotnet fsi
    System.IO.File.ReadAllText("/path/to/input-file");;
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    dotnet fsi
    System.Diagnostics.Process.Start("/bin/sh").WaitForExit();;
references:
- https://gtfobins.github.io/gtfobins/dotnet/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
