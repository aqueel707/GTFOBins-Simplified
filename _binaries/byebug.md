---
name: byebug
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
  command: byebug --no-stop /path/to/script.rb
  notes: ''
references:
- https://gtfobins.github.io/gtfobins/byebug/
tags:
- inherit
- ruby
---
