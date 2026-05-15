---
name: needrestart
capabilities:
- exec
required_permissions:
  level: user
  notes: Inherits behavior from perl.
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  notes: Chains to perl; OPSEC follows that binary's profile.
persistence_potential: false
examples:
- id: inherit
  description: Inherits attack surface from `perl` — see that entry.
  capabilities:
  - exec
  command: |-
    echo '...' >/path/to/temp-file
    needrestart -c /path/to/temp-file
  notes: This allows to run Perl code (`...`).
references:
- https://gtfobins.github.io/gtfobins/needrestart/
tags:
- inherit
- perl
---
