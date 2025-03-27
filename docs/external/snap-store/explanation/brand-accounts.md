(brand-accounts)=
# Brand accounts

Brand accounts are a key concept in Snap Stores. The Brand Account was set for your dedicated Snap Store at the time of store creation. The Brand Account defines the Brand (or company) scope of authority, and it must be used for certain functions.

The Brand account:

* Generates, registers and holds the signing keys for the Brand infrastructure.
* Signs Model Assertions used to build images that point at dedicated Snap Stores.
* May register [kernel](https://snapcraft.io/docs/the-kernel-snap) and [gadget](https://ubuntu.com/core/docs/gadget-snaps) snap names. Kernel and gadget snaps are special snaps that can only be published by a Brand Account. For that, the Brand Account must be given Publisher Role in the Base store. See the Ubuntu Core documentation for more information on [types of snaps](https://ubuntu.com/core/docs/snaps-in-ubuntu-core).

The use of the Brand Account and its credentials should be strictly limited. Canonical recommends that the Brand Account is assigned Roles that are truly needed. The Brand Account should not be a store Administrator, Reviewer or Viewer.

When the Brand Account generates keys, they are stored on the local disk in ( ~/.snap/gnupg). This account must be secured by the company using it. It is highly recommended that all accounts, and specifically the Brand and Administrator accounts [enable multi-factor authentication on their SSO accounts](https://help.ubuntu.com/community/SSO/FAQs/2FA).
