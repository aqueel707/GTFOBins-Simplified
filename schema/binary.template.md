---
# schema/binary.template.yaml
# Copy this file to _binaries/<name>.yaml and fill in all fields.
# Omit optional fields rather than leaving them blank.

name: ""                          # Exact binary name as it appears in PATH

capabilities:
  - exec                          # arbitrary command execution
  # - read                        # file read / exfil
  # - write                       # file write
  # - spawn                       # interactive shell
  # - upload                      # send data to remote
  # - download                    # fetch data from remote
  # - suid                        # exploitable when SUID bit is set
  # - sudo                        # exploitable via sudo rule
  # - bind                        # open listening socket
  # - reverse-shell               # initiate outbound shell

required_permissions:
  level: user                     # user | sudo | suid | root
  notes: ""                       # optional clarifying note (e.g. "needs --preserve-env")

difficulty: low                   # low | medium | high
# low    = one-liner, no setup, high reliability
# medium = requires environment condition or multi-step
# high   = needs specific version, race condition, or fragile chain

opsec:
  noise: low                      # low | medium | high — detection likelihood
  artifacts:
    - ""                          # files/logs written to disk (shell history, /var/log, etc.)
  notes: ""                       # free-text OPSEC guidance

persistence_potential: false      # true if binary can be used to establish persistence
persistence_notes: ""             # how (cron injection, authorized_keys write, etc.) — optional

examples:
  - id: exec-basic
    description: "Execute a command."
    capabilities: [exec]
    command: |
      BINARY_NAME -flag 'COMMAND'
    notes: ""                     # optional caveats for this specific example

  # - id: read-file
  #   description: "Read a file."
  #   capabilities: [read]
  #   command: |
  #     BINARY_NAME --read /path/to/file
  #   notes: ""

references:
  - ""                            # URLs, CVE IDs, or man page sections — optional

tags:
  - ""                            # arbitrary searchable tags — optional
---
