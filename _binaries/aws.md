---
name: aws
capabilities:
- read
required_permissions:
  level: user
difficulty: low
opsec:
  noise: low
  artifacts:
  - ~/.bash_history
  notes: ''
persistence_potential: false
examples:
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: aws ec2 describe-instances --filter file:///path/to/input-file
references:
- https://gtfobins.github.io/gtfobins/aws/
tags: []
---
