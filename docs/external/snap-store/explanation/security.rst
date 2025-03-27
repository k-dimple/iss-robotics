Dedicated Snap Store security
=============================

Dedicated Snap Stores are designed to ensure the secure distribution of software defined as snaps. To facilitate this distribution, a Dedicated Snap Store requires a few key pieces of information which are stored in different locations depending on the intended use of the information. This document exists to outline the various secrets which must be carefully handled to secure a Dedicated Snap Store, where those secrets live, and how they must be handled.

Secrets required for a functioning Dedicated Snap Store
-------------------------------------------------------

- Brand account credentials
  
  - Grants roles and privileges to the dedicated Snap Store, and is itself derived from a nominated `Ubuntu One SSO account <https://canonical-serial-vault.readthedocs-hosted.com/serial-vault/ubuntu-sso-accounts>`_.
  - It is **strongly recommended** that the Ubuntu SSO account is used only for Brand activities and that its use is strictly limited and controlled. It is recommended that the Brand account is only assigned the “Publisher” role.
- Signing keys
  
  - Used to sign `assertions <https://ubuntu.com/core/docs/reference/assertions>`_, which are digitally signed documents used for authentication and authorization throughout the snap ecosystem.
  - It is **recommended** to use a separate signing key for each type of assertion.
  - It is **recommended** to use `role-scoped keys <https://canonical-serial-vault.readthedocs-hosted.com/serial-vault/signing-keys/#register-a-signing-key-with-limited-roles>`_, which are limited to signing only specific assertion types and optionally only specific models.
- Other account credentials
  
  - Provides the use of roles to delegate control over various aspects of the snap lifecycle to specific Ubuntu One SSO accounts. For example, an account with the Reviewer role can review new snap uploads before they are eligible for publishing, but does not have the ability to publish snaps. Each SSO account can have multiple roles associated with it.

Location of secrets
-------------------

Stored by Canonical
*******************

- Serial Vault keys, used for signing specific assertions.

Stored by you
*************

- Brand account credentials
- Other account credentials
- Other snapcraft keys

How secrets are handled
-----------------------

By Canonical
************

- Canonical retains encrypted signing keys in the `Serial Vault <https://canonical-serial-vault.readthedocs-hosted.com/>`_ for signing specific assertions. The private keys cannot be accessed once generated or uploaded to the Serial Vault.

By you
******

- Account credentials should be stored and transmitted in a secure manner, for example by using a shared credential manager. Access to account credentials should only by given to individuals on an "as-needed" basis, and account credentials should be rotated regularly.
- Private keys should never be shared.
