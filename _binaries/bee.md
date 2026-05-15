---
name: bee
capabilities:
- exec
required_permissions:
  level: user
  notes: Inherits behavior from php.
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  notes: Chains to php; OPSEC follows that binary's profile.
persistence_potential: false
examples:
- id: inherit
  description: Inherits attack surface from `php` — see that entry.
  capabilities:
  - exec
  command: bee eval '...'
  notes: |-
    This allows to run PHP code (`...`).

    This must be excuted from the Backdrop CMS root directory (e.g. `/var/www/html`), alternatively use the `--root` option.
references:
- https://gtfobins.github.io/gtfobins/bee/
tags:
- inherit
- php
---
