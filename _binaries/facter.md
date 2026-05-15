---
name: facter
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
  command: FACTERLIB=/path/to/dir/ facter
  notes: The first `.rb` file in the `/path/to/dir/` directory will be executed.
- id: inherit-2
  description: Inherits attack surface from `ruby` — see that entry.
  capabilities:
  - exec
  command: facter --custom-dir=/path/to/dir/ x
  notes: The first `.rb` file in the `/path/to/dir/` directory will be executed.
references:
- https://gtfobins.github.io/gtfobins/facter/
tags:
- inherit
- ruby
---
