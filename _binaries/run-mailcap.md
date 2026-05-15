---
name: run-mailcap
capabilities:
- exec
required_permissions:
  level: user
  notes: Inherits behavior from less, vi.
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  notes: Chains to less, vi; OPSEC follows that binary's profile.
persistence_potential: false
examples:
- id: inherit
  description: Inherits attack surface from `less` — see that entry.
  capabilities:
  - exec
  command: run-mailcap --action=view text/plain:/etc/hosts
  notes: ''
- id: inherit-2
  description: Inherits attack surface from `vi` — see that entry.
  capabilities:
  - exec
  command: run-mailcap --action=edit text/plain:/path/to/output-file
  notes: The file must exist and be not empty.
references:
- https://gtfobins.github.io/gtfobins/run-mailcap/
tags:
- inherit
- less
- vi
---
