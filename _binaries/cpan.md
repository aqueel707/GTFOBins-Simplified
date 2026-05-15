---
name: cpan
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
    cpan
    ! ...
  notes: Perl code can be executed with the `!` command.
references:
- https://gtfobins.github.io/gtfobins/cpan/
tags:
- inherit
- perl
---
