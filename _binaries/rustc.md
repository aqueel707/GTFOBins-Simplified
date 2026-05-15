---
name: rustc
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
  notes: ''
persistence_potential: true
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: rustc /path/to/input-file
  notes: The compiler leaks some file lines in the compiler error.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    echo 'fn main() { println!("DATA"); }' >/path/to/temp-file
    rustc /path/to/temp-file -o /path/to/output-file
  notes: The comment appears in the compiled program.
references:
- https://gtfobins.github.io/gtfobins/rustc/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
