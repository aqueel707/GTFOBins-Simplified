---
name: exiftool
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
  command: |-
    exiftool -filename=/path/to/output-file /path/to/input-file
    cat /path/to/output-file
  notes: If the permissions allow it, files are moved (instead of copied) to the destination.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: exiftool -filename=/path/to/output-file /path/to/input-file
  notes: If the permissions allow it, files are moved (instead of copied) to the destination.
- id: file-write-2
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: exiftool "-description<=/path/to/input-file --filename /path/to/output-file
  notes: The output file must exists, either empty or be a supported image file. The content is written amidst other content.
- id: file-write-3
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: exiftool "-description=DATA --filename /path/to/output-file
  notes: The output file must exists, either empty or be a supported image file. The content is written amidst other content.
- id: file-write-4
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: exiftool -description -W /path/to/output-file --filename /path/to/input-file
  notes: Writes the metadata tags of the input file in textual format to the output.
references:
- https://gtfobins.github.io/gtfobins/exiftool/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
