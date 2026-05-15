---
name: wireshark
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
    wireshark -c 1 -i lo -k -f 'udp port 12345' &
    echo DATA | nc -u 127.127.127.127 12345
  notes: |-
    This technique can be used to write arbitrary files, i.e., the dump of one UDP packet.

    After starting Wireshark, and waiting for the capture to begin, deliver the UDP packet, e.g., with `nc` (see below). The capture then stops and the packet dump can be saved:

    1. select the only received packet;

    2. right-click on "Data" from the "Packet Details" pane, and select "Export Packet Bytes...";

    3. choose where to save the packet dump.
references:
- https://gtfobins.github.io/gtfobins/wireshark/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
