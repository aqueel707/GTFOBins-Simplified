---
name: vigr
capabilities:
- exec
required_permissions:
  level: user
  notes: Inherits behavior from vi.
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  notes: Chains to vi; OPSEC follows that binary's profile.
persistence_potential: false
examples:
- id: inherit
  description: Inherits attack surface from `vi` — see that entry.
  capabilities:
  - exec
  command: vigr
  notes: Despite requiring superuser privileges to run, the editor is executed as the unprivileged user.
references:
- https://gtfobins.github.io/gtfobins/vigr/
tags:
- inherit
- vi
---
