---
name: hashcat
capabilities:
- write
required_permissions:
  level: user
difficulty: low
opsec:
  noise: low
  artifacts:
  - ~/.bash_history
  - File timestamps / inotify events on target paths
  notes: ''
persistence_potential: true
examples:
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    echo -n DATA | tee /path/to/wordlist | md5sum | awk '{print $1}' >/path/to/hash
    hashcat -m 0 --quiet --potfile-disable -o /path/to/output-file --outfile-format=2 --outfile-autohex-disable /path/to/hash /path/to/wordlist
  notes: Append data to the end of the output file, creating if does not exist.
references:
- https://gtfobins.github.io/gtfobins/hashcat/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
