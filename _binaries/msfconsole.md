---
name: msfconsole
capabilities:
- exec
required_permissions:
  level: user
  notes: Inherits behavior from irb.
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  notes: Chains to irb; OPSEC follows that binary's profile.
persistence_potential: false
examples:
- id: inherit
  description: Inherits attack surface from `irb` — see that entry.
  capabilities:
  - exec
  command: |-
    msfconsole
    irb
  notes: ''
references:
- https://gtfobins.github.io/gtfobins/msfconsole/
tags:
- inherit
- irb
---
