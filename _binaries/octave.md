---
name: octave
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
  notes: The payloads are compatible with GUI mode.
persistence_potential: true
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: octave-cli --eval 'format none; fid = fopen("/path/to/input-file"); while(!feof(fid)); txt = fgetl(fid); disp(txt); endwhile; fclose(fid);'
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: octave-cli --eval 'fid = fopen("/path/to/output-file", "w"); fputs(fid, "DATA"); fclose(fid);'
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: octave-cli --eval 'system("/bin/sh")'
references:
- https://gtfobins.github.io/gtfobins/octave/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
