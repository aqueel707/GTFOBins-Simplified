---
name: irb
capabilities:
- exec
required_permissions:
  level: user
  notes: Inherits behavior from ruby.
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  notes: Chains to ruby; OPSEC follows that binary's profile.
persistence_potential: false
examples:
- id: inherit
  description: Inherits attack surface from `ruby` — see that entry.
  capabilities:
  - exec
  command: |-
    irb
    ...
  notes: This allows to run Ruby code (`...`).
references:
- https://gtfobins.github.io/gtfobins/irb/
tags:
- inherit
- ruby
---
