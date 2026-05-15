---
name: file
capabilities:
- read
required_permissions:
  level: user
difficulty: low
opsec:
  noise: low
  artifacts:
  - ~/.bash_history
  notes: ''
persistence_potential: false
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: file -f /path/to/input-file
  notes: Each input line is treated as a filename for the `file` command and the output is corrupted by a suffix `:` followed by the result or the error of the operation.
- id: file-read-2
  description: Read an arbitrary file.
  capabilities:
  - read
  command: file -m /path/to/input-file
  notes: |-
    Each line is corrupted by a prefix string and wrapped inside quotes.

    If a line in the target file begins with a `#`, it will not be printed as these lines are parsed as comments.

    It can also be provided with a directory and will read each file in the directory.
references:
- https://gtfobins.github.io/gtfobins/file/
tags: []
---
