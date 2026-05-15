---
name: apport-cli
capabilities:
- exec
required_permissions:
  level: user
  notes: Inherits behavior from less.
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  notes: Chains to less; OPSEC follows that binary's profile.
persistence_potential: false
examples:
- id: inherit
  description: Inherits attack surface from `less` — see that entry.
  capabilities:
  - exec
  command: |-
    apport-cli -f
    1
    2
    v
  notes: The terminal interface expects some choices in order to spawn tha pager.
references:
- https://gtfobins.github.io/gtfobins/apport-cli/
tags:
- inherit
- less
---
