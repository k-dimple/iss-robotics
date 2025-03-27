(profiles)=
# How to use profiles

Profiles store a set of configuration options.
They can contain {ref}`instance-options`, {ref}`devices`, and device options.

You can apply any number of profiles to an instance.
They are applied in the order they are specified, so the last profile to specify a specific key takes precedence.
However, instance-specific configuration always overrides the configuration coming from the profiles.

```{note}
Profiles can be applied to containers and virtual machines.
Therefore, they might contain options and devices that are valid for either type.

When applying a profile that contains configuration that is not suitable for the instance type, this configuration is ignored and does not result in an error.
```

If you don't specify any profiles when launching a new instance, the `default` profile is applied automatically.
This profile defines a network interface and a root disk.
The `default` profile cannot be renamed or removed.

## View profiles

````{tabs}
```{group-tab} CLI
Enter the following command to display a list of all available profiles:

    lxc profile list

Enter the following command to display the contents of a profile:

    lxc profile show <profile_name>
```
```{group-tab} API
To display all available profiles, send a request to the `/1.0/profiles` endpoint:

    lxc query --request GET /1.0/profiles?recursion=1

To display a specific profile, send a request to that profile:

    lxc query --request GET /1.0/profiles/<profile_name>

See [`GET /1.0/profiles`](swagger:/profiles/profiles_get) and [`GET /1.0/profiles/{name}`](swagger:/profiles/profile_get) for more information.
```
```{group-tab} UI
Go to the {guilabel}`Profiles` section to view all available profiles.

To view information about a specific profile, click its line in the overview.
To display the full information about a profile, including its configuration, click the profile name to go to the profile detail page.
```
````

## Create an empty profile

````{tabs}
```{group-tab} CLI
Enter the following command to create an empty profile:

    lxc profile create <profile_name>
```
```{group-tab} API
To create an empty profile, send a POST request to the `/1.0/profiles` endpoint:

    lxc query --request POST /1.0/profiles --data '{"name": "<profile_name>"}'

See [`POST /1.0/profiles`](swagger:/profiles/profiles_post) for more information.
```
```{group-tab} UI
To create a profile, go to the {guilabel}`Profiles` section and click {guilabel}`Create profile`.

Enter at least a profile name and click {guilabel}`Create` to save the new profile.
```
````

(profiles-edit)=
## Edit a profile

You can either set specific configuration options for a profile or edit the full profile.
See {ref}`instance-config` (and its subpages) for the available options.

(profiles-set-options)=
### Set specific options for a profile

````{tabs}
```{group-tab} CLI
To set an instance option for a profile, use the [`lxc profile set`](lxc_profile_set.md) command.
Specify the profile name and the key and value of the instance option:

    lxc profile set <profile_name> <option_key>=<option_value> <option_key>=<option_value> ...

To add and configure an instance device for your profile, use the [`lxc profile device add`](lxc_profile_device_add.md) command.
Specify the profile name, a device name, the device type and maybe device options (depending on the {ref}`device type <devices>`):

    lxc profile device add <profile_name> <device_name> <device_type> <device_option_key>=<device_option_value> <device_option_key>=<device_option_value> ...

To configure instance device options for a device that you have added to the profile earlier, use the [`lxc profile device set`](lxc_profile_device_set.md) command:

    lxc profile device set <profile_name> <device_name> <device_option_key>=<device_option_value> <device_option_key>=<device_option_value> ...
```
```{group-tab} API
To set an instance option for a profile, send a PATCH request to the profile.
Specify the key and value of the instance option under the `"config"` field:

    lxc query --request PATCH /1.0/profiles/<profile_name> --data '{
      "config": {
        "<option_key>": "<option_value>",
        "<option_key>": "<option_value>"
      }
    }'

To add and configure an instance device for your profile, specify the device name, the device type and maybe device options (depending on the {ref}`device type <devices>`) under the `"devices"` field:

    lxc query --request PATCH /1.0/profiles/<profile_name> --data '{
      "devices": {
        "<device_name>": {
          "type": "<device_type>",
          "<device_option_key>": "<device_option_value>",
          "<device_option_key>": "<device_option_value>"
        }
      }
    }'

See [`PATCH /1.0/profiles/{name}`](swagger:/profiles/profile_patch) for more information.
```
```{group-tab} UI
To configure a profile, select it from the {guilabel}`Profiles` overview, switch to the {guilabel}`Configuration` tab and click {guilabel}`Edit profile`.
You can then configure options for the profile in the same way as you {ref}`configure instance options <instances-configure-options>`.
```
````

### Edit the full profile

Instead of setting each configuration option separately, you can provide all options at once.

Check the contents of an existing profile or instance configuration for the required fields.
For example, the `default` profile might look like this:

    config: {}
    description: Default LXD profile
    devices:
      eth0:
        name: eth0
        network: lxdbr0
        type: nic
      root:
        path: /
        pool: default
        type: disk
    name: default
    used_by:

Instance options are provided as an array under `config`.
Instance devices and instance device options are provided under `devices`.

`````{tabs}
````{group-tab} CLI
To edit a profile using your standard terminal editor, enter the following command:

    lxc profile edit <profile_name>

Alternatively, you can create a YAML file (for example, `profile.yaml`) with the configuration and write the configuration to the profile with the following command:

    lxc profile edit <profile_name> < profile.yaml
````
````{group-tab} API
To update the entire profile configuration, send a PUT request to the profile:

    lxc query --request PUT /1.0/profiles/<profile_name> --data '{
      "config": { ... },
      "description": "<description>",
      "devices": { ... }
    }'

See [`PUT /1.0/profiles/{name}`](swagger:/profiles/profile_put) for more information.
````
````{group-tab} UI
To edit the YAML configuration of a profile, go to the profile detail page, switch to the {guilabel}`Configuration` tab and select {guilabel}`YAML configuration`.
Then click {guilabel}`Edit profile`.

Edit the YAML configuration as required.
Then click {guilabel}`Save changes` to save the updated configuration.

```{important}
When doing updates, do not navigate away from the YAML configuration without saving your changes.
If you do, your updates are lost.
```
````
`````

## Apply a profile to an instance

`````{tabs}
````{group-tab} CLI
Enter the following command to apply a profile to an instance:

    lxc profile add <instance_name> <profile_name>

```{tip}
Check the configuration after adding the profile: [`lxc config show <instance_name>`](lxc_config_show.md)

You will see that your profile is now listed under `profiles`.
However, the configuration options from the profile are not shown under `config` (unless you add the `--expanded` flag).
The reason for this behavior is that these options are taken from the profile and not the configuration of the instance.

This means that if you edit a profile, the changes are automatically applied to all instances that use the profile.
```

You can also specify profiles when launching an instance by adding the `--profile` flag:

    lxc launch <image> <instance_name> --profile <profile> --profile <profile> ...
````
````{group-tab} API
To apply a profile to an instance, add it to the profile list in the instance configuration:

    lxc query --request PATCH /1.0/instances/<instance_name> --data '{
      "profiles": [ "default", "<profile_name>" ]
    }'

See [`PATCH /1.0/instances/{name}`](swagger:/instances/instance_patch) for more information.

You can also specify profiles when {ref}`creating an instance <instances-create>`:

    lxc query --request POST /1.0/instances --data '{
      "name": "<instance_name>",
      "profiles": [ "default", "<profile_name>" ],
      "source": {
        "alias": "<image_alias>",
        "protocol": "simplestreams",
        "server": "<server_URL>",
        "type": "image"
      }
    }'
````
```{group-tab} UI
To apply a profile to an instance, select the instance from the {guilabel}`Instances` overview, switch to the {guilabel}`Configuration` tab and click {guilabel}`Edit instance`.
You can then select a profile from the drop-down list, or click {guilabel}`Add profile` to attach another profile in addition to the one (or more) that are already attached to the instance.

If you attach more than one profile to an instance, you can specify the order in which the profiles are applied by moving each profile up or down the list.

You can also apply profiles in the same way when {ref}`creating an instance <instances-create>`.
```
`````

## Remove a profile from an instance

````{tabs}
```{group-tab} CLI
Enter the following command to remove a profile from an instance:

    lxc profile remove <instance_name> <profile_name>
```
```{group-tab} API
To remove a profile from an instance, send a PATCH request to the instance configuration with the new profile list.
For example, to revert back to using only the default profile:

    lxc query --request PATCH /1.0/instances/<instance_name> --data '{
      "profiles": [ "default" ]
    }'

See [`PATCH /1.0/instances/{name}`](swagger:/instances/instance_patch) for more information.
```
```{group-tab} UI
To remove a profile from an instance, select the instance from the {guilabel}`Instances` overview, switch to the {guilabel}`Configuration` tab and click {guilabel}`Edit instance`.
Click the {guilabel}`Delete` link next to a profile to remove it from the instance.
```
````
