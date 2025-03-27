---
discourse: lxc:[Cgroup2&#32;related&#32;issue](14705)
---

# Frequently asked questions

The following sections give answers to frequently asked questions.
They explain how to resolve common issues and point you to more detailed information.

## Why do my instances not have network access?

Most likely, your firewall blocks network access for your instances.
See {ref}`network-bridge-firewall` for more information about the problem and how to fix it.

Another frequent reason for connectivity issues is running LXD and Docker on the same host.
See {ref}`network-lxd-docker` for instructions on how to fix such issues.

## How to enable the LXD server for remote access?

By default, the LXD server is not accessible from the network, because it only listens on a local Unix socket.

You can enable it for remote access by following the instructions in {ref}`server-expose`.

## When I do a `lxc remote add`, it asks for a token?

To be able to access the remote API, clients must authenticate with the LXD server.

See {ref}`server-authenticate` for instructions on how to authenticate using a trust token.

## Why should I not run privileged containers?

A privileged container can do things that affect the entire host - for example, it can use things in `/sys` to reset the network card, which will reset it for the entire host, causing network blips.
See {ref}`container-security` for more information.

Almost everything can be run in an unprivileged container, or - in cases of things that require unusual privileges, like wanting to mount NFS file systems inside the container - you might need to use bind mounts.

## Can I bind-mount my home directory in a container?

Yes, you can do this by using a {ref}`disk device <devices-disk>`:

    lxc config device add container-name home disk source=/home/${USER} path=/home/ubuntu

For unprivileged containers, you need to make sure that the user in the container has working read/write permissions.
Otherwise, all files will show up as the overflow UID/GID (`65536:65536`) and access to anything that's not world-readable will fail.
Use either of the following methods to grant the required permissions:

- Pass `shift=true` to the [`lxc config device add`](lxc_config_device_add.md) call. This depends on the kernel and file system supporting either idmapped mounts (see [`lxc info`](lxc_info.md)).
- Add a `raw.idmap` entry (see [Idmaps for user namespace](userns-idmap.md)).
- Place recursive POSIX ACLs on your home directory.

Privileged containers do not have this issue because all UID/GID in the container are the same as outside.
But that's also the cause of most of the security issues with such privileged containers.

## How can I run Docker inside a LXD container?

```{youtube} https://www.youtube.com/watch?v=_fCSSEyiGro
```

To run Docker inside a LXD container, set the {config:option}`instance-security:security.nesting` option of the container to `true`:

    lxc config set <container> security.nesting true

If you plan to use the OverlayFS storage driver in Docker, you should also set the {config:option}`instance-security:security.syscalls.intercept.mknod` and {config:option}`instance-security:security.syscalls.intercept.setxattr` options to `true`.
See [`mknod` / `mknodat`](syscall-mknod) and [`setxattr`](syscall-setxattr) for more information.

Note that LXD containers cannot load kernel modules, so depending on your Docker configuration, you might need to have extra kernel modules loaded by the host.
You can do so by setting a comma-separated list of kernel modules that your container needs:

    lxc config set <container_name> linux.kernel_modules <modules>

In addition, creating a `/.dockerenv` file in your container can help Docker ignore some errors it's getting due to running in a nested environment.

## Where does the LXD client (`lxc`) store its configuration?

The [`lxc`](lxc.md) command stores its configuration under `~/.config/lxc`, or in `~/snap/lxd/common/config` for snap users.

Various configuration files are stored in that directory, for example:

- `client.crt`: client certificate (generated on demand)
- `client.key`: client key (generated on demand)
- `config.yml`: configuration file (info about `remotes`, `aliases`, etc.)
- `servercerts/`: directory with server certificates belonging to `remotes`

## Why can I not ping my LXD instance from another host?

Many switches do not allow MAC address changes, and will either drop traffic with an incorrect MAC or disable the port totally.
If you can ping a LXD instance from the host, but are not able to ping it from a different host, this could be the cause.

The way to diagnose this problem is to run a `tcpdump` on the uplink and you will see either ``ARP Who has `xx.xx.xx.xx` tell `yy.yy.yy.yy` ``, with you sending responses but them not getting acknowledged, or ICMP packets going in and out successfully, but never being received by the other host.

(faq-monitor)=
## How can I monitor what LXD is doing?

To see detailed information about what LXD is doing and what processes it is running, use the [`lxc monitor`](lxc_monitor.md) command.

For example, to show a human-readable output of all types of messages, enter the following command:

    lxc monitor --pretty

See [`lxc monitor --help`](lxc_monitor.md) for all options, and {doc}`debugging` for more information.

## Why does LXD stall when creating an instance?

Check if your storage pool is out of space (by running [`lxc storage info <pool_name>`](lxc_storage_info.md)).
In that case, LXD cannot finish unpacking the image, and the instance that you're trying to create shows up as stopped.

To get more insight into what is happening, run [`lxc monitor`](lxc_monitor.md) (see {ref}`faq-monitor`), and check `sudo dmesg` for any I/O errors.

## Why does starting containers suddenly fail?

If starting containers suddenly fails with a cgroup-related error message (`Failed to mount "/sys/fs/cgroup"`), this might be due to running a VPN client on the host.

This is a known issue for both [Mullvad VPN](https://github.com/mullvad/mullvadvpn-app/issues/3651) and [Private Internet Access VPN](https://github.com/pia-foss/desktop/issues/50), but might occur for other VPN clients as well.
The problem is that the VPN client mounts the `net_cls` cgroup1 over cgroup2 (which LXD uses).

The easiest fix for this problem is to stop the VPN client and unmount the `net_cls` cgroup1 with the following command:

    umount /sys/fs/cgroup/net_cls

If you need to keep the VPN client running, mount the `net_cls` cgroup1 in another location and reconfigure your VPN client accordingly.
See [this Discourse post](https://discuss.linuxcontainers.org/t/help-help-help-cgroup2-related-issue-on-ubuntu-jammy-with-mullvad-and-privateinternetaccess-vpn/14705/18) for instructions for Mullvad VPN.

## Why does LXD not start on Ubuntu 20.04 LTS or earlier?

If you are running LXD on Ubuntu 20.04 LTS or earlier, you might be missing support for ZFS 2.1 in the kernel (see the {ref}`requirements <requirements-zfs>`).

If LXD fails to start, check the `/var/snap/lxd/common/lxd/logs/lxd.log` log file for the following error to see if the reason is missing ZFS support:

    Error: Required tool ‘zpool’ is missing

If you are on Ubuntu 20.04 LTS, you can resolve the issue by installing the HWE kernel and rebooting the nodes to provide the required kernel drivers for ZFS 2.1:

    sudo apt-get update
    sudo apt-get install linux-generic-hwe-20.04

If you are on earlier versions of Ubuntu, you should use a compatible LTS release of LXD.
