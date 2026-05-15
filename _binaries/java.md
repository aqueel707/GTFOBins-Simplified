---
name: java
capabilities:
- exec
- spawn
required_permissions:
  level: user
difficulty: low
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  notes: ''
persistence_potential: true
examples:
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: java Shell
  notes: |-
    The `Shell.class` class file can be compiled offline, then uploaded to the target:

    ```
    cat >Shell.java <<EOF
    public class Shell {
        public static void main(String[] args) throws Exception {
            new ProcessBuilder("/bin/sh").inheritIO().start().waitFor();
        }
    }
    EOF

    javac Shell.java
    ```
references:
- https://gtfobins.github.io/gtfobins/java/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
