---
name: cowsay
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
  command: cowsay -f /path/to/script.pl x
  notes: ''
references:
- https://gtfobins.github.io/gtfobins/cowsay/
tags:
- inherit
- perl
---
