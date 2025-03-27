# Environment variables

The LXD client and daemon respect some environment variables to adapt to
the user's environment and to turn some advanced features on and off.

```{note}
These environment variables are not available if you use the LXD snap.
```

## Common

Name                            | Description
:---                            | :----
`LXD_DIR`                       | The LXD data directory
`PATH`                          | List of paths to look into when resolving binaries
`http_proxy`                    | Proxy server URL for HTTP
`https_proxy`                   | Proxy server URL for HTTPS
`no_proxy`                      | List of domains, IP addresses or CIDR ranges that don't require the use of a proxy

## Client environment variable

Name                            | Description
:---                            | :----
`EDITOR`                        | What text editor to use
`VISUAL`                        | What text editor to use (if `EDITOR` isn't set)
`LXD_CONF`                      | Path to the LXC configuration directory
`LXD_GLOBAL_CONF`               | Path to the global LXC configuration directory
`LXC_REMOTE`                    | Name of the remote to use (overrides configured default remote)

## Server environment variable

Name                            | Description
:---                            | :----
`LXD_EXEC_PATH`                 | Full path to the LXD binary (used when forking subcommands)
`LXD_LXC_TEMPLATE_CONFIG`       | Path to the LXC template configuration directory
`LXD_SECURITY_APPARMOR`         | If set to `false`, forces AppArmor off
`LXD_UNPRIVILEGED_ONLY`         | If set to `true`, enforces that only unprivileged containers can be created. Note that any privileged containers that have been created before setting LXD_UNPRIVILEGED_ONLY will continue to be privileged. To use this option effectively it should be set when the LXD daemon is first set up.
`LXD_OVMF_PATH`                 | Path to an OVMF build including `OVMF_CODE.fd` and `OVMF_VARS.ms.fd` (deprecated, please use `LXD_QEMU_FW_PATH` instead)
`LXD_QEMU_FW_PATH`              | Path (or `:` separated list of paths) to firmware (OVMF, SeaBIOS) to be used by QEMU
`LXD_IDMAPPED_MOUNTS_DISABLE`   | Disable idmapped mounts support (useful when testing traditional UID shifting)
`LXD_DEVMONITOR_DIR`            | Path to be monitored by the device monitor. This is primarily for testing.
`LXD_FSMONITOR_DRIVER`          | Driver to be used for file system monitoring. This is primarily for testing.
