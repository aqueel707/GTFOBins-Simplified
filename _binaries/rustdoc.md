---
name: rustdoc
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
  command: rustdoc /path/to/input-file
  notes: Partial content is displayed as error messages.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    echo '//! DATA' >/path/to/temp-file
    rustdoc /path/to/temp-file -o /path/to/output-dir/
  notes: This command creates a number of documentation files in the target directory, and the data is written in multiple locations, e.g., `src/temp_file/temp-file.html`, amidst other content.
references:
- https://gtfobins.github.io/gtfobins/rustdoc/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
