(first-steps)=
# First steps with LXD

````{only} integrated

```{note}
MicroCloud users can disregard the instructions on this page, because the MicroCloud setup process handles the installation and initialization of LXD.
```

````

This tutorial guides you through the first steps with LXD.
It covers installing and initializing LXD, creating and configuring some instances, interacting with the instances, and creating snapshots.

After going through these steps, you will have a general idea of how to use LXD, and you can start exploring more advanced use cases!

```{note}
Ensure that you have 20 GiB free disk space before starting this tutorial.
```

<!-- Include start tutorial installation -->

## Install and initialize LXD

The easiest way to install LXD is to install the snap package.
If you prefer a different installation method, or use a Linux distribution that is not supported by the snap package, see {ref}`installing`.

1. Install `snapd`:

   1. Run `snap version` to find out if snap is installed on your system:

      ```{terminal}
      :input: snap version

      snap    2.63+24.04ubuntu0.1
      snapd   2.63+24.04ubuntu0.1
      series  16
      ubuntu  24.04
      kernel  5.15.0-117-generic
      ```

      If you see a table of version numbers, snap is installed and you can continue with the next step of installing LXD.

   1. If the command returns an error, run the following commands to install the latest version of ``snapd`` on Ubuntu:

          sudo apt update
          sudo apt install snapd

      ```{note}
      For other Linux distributions, see the [installation instructions](https://snapcraft.io/docs/installing-snapd) in the Snapcraft documentation.
      ```

1. Enter the following command to install LXD:

       sudo snap install lxd

   If you get an error message that the LXD snap is already installed, run the following command to refresh it and ensure that you are running an up-to-date version:

       sudo snap refresh lxd

1. Check if the current user is part of the `lxd` group (the group was automatically created during the previous step):

       getent group lxd | grep "$USER"

   If this command returns a result, you're set up correctly and can continue with the next step.

   If there is no result, enter the following commands to add the current user to the `lxd` group (which is needed to grant the user permission to interact with LXD):

       sudo usermod -aG lxd "$USER"
       newgrp lxd

1. Enter the following command to initialize LXD:

       lxd init --minimal

   This will create a minimal setup with default options.
   If you want to tune the initialization options, see {ref}`initialize` for more information.

<!-- Include end tutorial installation -->

## Launch and inspect instances

LXD is image based and can load images from different image servers.
In this tutorial, we will use the official [`ubuntu:`](https://cloud-images.ubuntu.com/releases/) image server.

You can list all images (long list) that are available on this image server with:

    lxc image list ubuntu:

You can list the images used in this tutorial with:

    lxc image list ubuntu: 24.04 architecture=$(uname -m)

See {ref}`images` for more information about the images that LXD uses.

Now, let's start by launching a few instances.
With *instance*, we mean either a container or a virtual machine.
See {ref}`containers-and-vms` for information about the difference between the two instance types.

For managing instances, we use the LXD command line client `lxc`.
See [About `lxd` and `lxc`](lxd-lxc) if you are confused about when to use the `lxc` command and when to use the `lxd` command.

1. Launch a container called `first` using the Ubuntu 24.04 LTS image:

       lxc launch ubuntu:24.04 first

   ```{note}
   Launching this container takes a few seconds, because the image must be downloaded and unpacked first.
   ```

1. Launch a container called `second` using the same image:

       lxc launch ubuntu:24.04 second

   ```{note}
   Launching this container is quicker than launching the first, because the image is already available locally.
   ```

1. Copy the first container into a container called `third`:

       lxc copy first third

1. Launch a VM called `ubuntu-vm` using the Ubuntu 24.04 LTS image:

       lxc launch ubuntu:24.04 ubuntu-vm --vm

   ```{note}
   Even though you are using the same image name to launch the instance, LXD downloads a slightly different image that is compatible with VMs.
   ```

1. Check the list of instances that you launched:

       lxc list

   You will see that all but the third container are running.
   This is because you created the third container by copying the first, but you didn't start it.

   You can start the third container with:

       lxc start third

1. Query more information about each instance with:

       lxc info first
       lxc info second
       lxc info third
       lxc info ubuntu-vm

1. We don't need all of these instances for the remainder of the tutorial, so let's clean some of them up:

   1. Stop the second container:

          lxc stop second

   1. Delete the second container:

          lxc delete second

   1. Delete the third container:

          lxc delete third

      Since this container is running, you get an error message that you must stop it first.
      Alternatively, you can force-delete it:

          lxc delete third --force

See {ref}`instances-create` and {ref}`instances-manage` for more information.

## Configure instances

There are several limits and configuration options that you can set for your instances.
See {ref}`instance-options` for an overview.

Let's create another container with some resource limits:

1. Launch a container and limit it to one vCPU and 192 MiB of RAM:

       lxc launch ubuntu:24.04 limited --config limits.cpu=1 --config limits.memory=192MiB

1. Check the current configuration and compare it to the configuration of the first (unlimited) container:

       lxc config show limited
       lxc config show first

1. Check the amount of free and used memory on the parent system and on the two containers:

       free -m
       lxc exec first -- free -m
       lxc exec limited -- free -m

   ```{note}
   The total amount of memory is identical for the parent system and the first container, because by default, the container inherits the resources from its parent environment.
   The limited container, on the other hand, has only 192 MiB available.
   ```

1. Check the number of CPUs available on the parent system and on the two containers:

       nproc
       lxc exec first -- nproc
       lxc exec limited -- nproc

   ```{note}
   Again, the number is identical for the parent system and the first container, but reduced for the limited container.
   ```

1. You can also update the configuration while your container is running:

   1. Configure a memory limit for your container:

          lxc config set limited limits.memory=128MiB

   1. Check that the configuration has been applied:

          lxc config show limited

   1. Check the amount of memory that is available to the container:

          lxc exec limited -- free -m

      Note that the number has changed.

1. Depending on the instance type and the storage drivers that you use, there are more configuration options that you can specify.
   For example, you can configure the size (quota) of the root disk device for a VM:

   1. Check the current size of the root disk device of the Ubuntu VM:

      ```{terminal}
      :input: lxc exec ubuntu-vm -- df -h

      Filesystem      Size  Used Avail Use% Mounted on
      /dev/root       9.6G  1.4G  8.2G  15% /
      tmpfs           483M     0  483M   0% /dev/shm
      tmpfs           193M  604K  193M   1% /run
      tmpfs           5.0M     0  5.0M   0% /run/lock
      tmpfs            50M   14M   37M  27% /run/lxd_agent
      /dev/sda15      105M  6.1M   99M   6% /boot/efi
      ```

   1. Override the size of the root disk device:

          lxc config device override ubuntu-vm root size=30GiB

   1. Restart the VM:

          lxc restart ubuntu-vm

   1. Check the size of the root disk device again:

       ```{terminal}
       :input: lxc exec ubuntu-vm -- df -h

       Filesystem      Size  Used Avail Use% Mounted on
       /dev/root        29G  1.4G   28G   5% /
       tmpfs           483M     0  483M   0% /dev/shm
       tmpfs           193M  588K  193M   1% /run
       tmpfs           5.0M     0  5.0M   0% /run/lock
       tmpfs            50M   14M   37M  27% /run/lxd_agent
       /dev/sda15      105M  6.1M   99M   6% /boot/efi
       ```

See {ref}`instances-configure` and {ref}`instance-config` for more information.

## Interact with instances

You can interact with your instances by running commands in them (including an interactive shell) or accessing the files in the instance.

Start by launching an interactive shell in your instance:

1. Run the `bash` command in your container:

       lxc exec first -- bash

1. Enter some commands, for example, display information about the operating system:

       cat /etc/*release

1. Exit the interactive shell:

       exit

Instead of logging on to the instance and running commands there, you can run commands directly from the host.

For example, you can install a command line tool on the instance and run it:

    lxc exec first -- apt-get update
    lxc exec first -- apt-get install sl -y
    lxc exec first -- /usr/games/sl

See {ref}`run-commands` for more information.

You can also access the files from your instance and interact with them:

1. Pull a file from the container:

       lxc file pull first/etc/hosts .

1. Add an entry to the file:

       echo "1.2.3.4 my-example" >> hosts

1. Push the file back to the container:

       lxc file push hosts first/etc/hosts

1. Use the same mechanism to access log files:

       lxc file pull first/var/log/syslog - | less

   ```{note}
   Press `q` to exit the `less` command.
   ```

See {ref}`instances-access-files` for more information.

## Manage snapshots

You can create a snapshot of your instance, which makes it easy to restore the instance to a previous state.

1. Create a snapshot called "clean":

       lxc snapshot first clean

1. Confirm that the snapshot has been created:

       lxc list first
       lxc info first

   ```{note}
   `lxc list` shows the number of snapshots.
   `lxc info` displays information about each snapshot.
   ```

1. Break the container:

       lxc exec first -- rm /usr/bin/bash

1. Confirm the breakage:

       lxc exec first -- bash

   ```{note}
   You do not get a shell, because you deleted the `bash` command.
   ```

1. Restore the container to the state of the snapshot:

       lxc restore first clean

1. Confirm that everything is back to normal:

       lxc exec first -- bash
       exit

1. Delete the snapshot:

       lxc delete first/clean

See {ref}`instances-snapshots` for more information.

<!-- Include start tutorial next steps -->

## Next steps

Now that you've done your first experiments with LXD, you should read up on important concepts in the {ref}`explanation` section and check out the {ref}`howtos` to start working with LXD!

<!-- Include end tutorial next steps -->
