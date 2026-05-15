---
name: batcat
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
  command: batcat --paging always /etc/hosts
  notes: '`--paging always` can be omitted provided that the output doesn''t fit the screen.'
references:
- https://gtfobins.github.io/gtfobins/batcat/
tags:
- inherit
- less
---
