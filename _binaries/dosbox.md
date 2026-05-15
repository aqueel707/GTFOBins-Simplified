---
name: dosbox
capabilities:
- read
- write
required_permissions:
  level: user
difficulty: low
opsec:
  noise: low
  artifacts:
  - ~/.bash_history
  - File timestamps / inotify events on target paths
  notes: Basically `dosbox` allows to mount the local file system, so that it can be altered using DOS commands. Note that the DOS filename convention ([8.3](https://en.wikipedia.org/wiki/8.3_filename)) is used.
persistence_potential: true
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: dosbox -c 'mount c /' -c 'type c:\path\to\input'
  notes: The file content will be displayed in the DOSBox graphical window.
- id: file-read-2
  description: Read an arbitrary file.
  capabilities:
  - read
  command: |-
    dosbox -c 'mount c /' -c 'copy c:\path\to\input c:\path\to\output' -c exit
    cat /path/to/OUTPUT
  notes: The file is copied to a readable location.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: dosbox -c 'mount c /' -c "echo DATA >c:\path\to\output" -c exit
  notes: Note that `echo` terminates the string with a DOS-style line terminator (`\r\n`), if that's a problem and your scenario allows it, you can create the file outside `dosbox`, then use `copy` to do the actual write.
references:
- https://gtfobins.github.io/gtfobins/dosbox/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
