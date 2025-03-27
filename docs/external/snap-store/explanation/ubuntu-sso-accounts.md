(ubuntu-sso-accounts)=
# Ubuntu SSO accounts

Store roles and privileges can be granted to an Ubuntu SSO account.

For example, a dedicated Snap Store is administered by an account that is granted the [Administrator Role](project:#setting-up-account-roles). New snap names are registered by accounts with the [Publisher Role](project:#setting-up-account-roles). A developer can upload snaps to a private Store with the Publisher role, or as a [Collaborator](project:#setting-up-account-roles) on a specific snap.

Ubuntu SSO accounts can be assigned SSH and GPG keys. Store [assertions](https://snapcraft.io/docs/assertions) should be signed by keys registered to an account. Ubuntu SSO accounts also authenticate users to [Launchpad](https://launchpad.net), the [Snapcraft forum](https://forum.snapcraft.io), and many more sites and services.

Anyone can create an Ubuntu SSO account at https://login.ubuntu.com. Each account requires a dedicated email address. You can then see additional account data on the [Snapcraft dashboard](https://dashboard.snapcraft.io/dev/account/).

Here are a few points to note regarding Ubuntu SSO accounts:

* It is highly recommended to generate a SSH key and upload a public SSH part to your Ubuntu account. Among other things, this enables you to [log onto Ubuntu Core devices](https://ubuntu.com/core/docs/system-user) on first boot over SSH.
* Note the Ubuntu SSO account’s account-id. This is a critical identifier that is used in many parts of the Snap Store ecosystem.
* When you are logged into snapcraft and run `snapcraft whoami`, the account ID is displayed as the developer-id:

```

$ snapcraft whoami

email: thisis@theaccountemail.com

developer-id: THIS_IS_THE_ACCOUNT_ID

```
