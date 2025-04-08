Dedicated Snap Store configuration
==================================

{% if 'admin@acme.com' in CUSTOMER_ADMIN_EMAIL %}
.. warning:: 

  Example values are provided for store configuration in this document. If you are a Dedicated Snap Store customer, you will be provided with a set of documentation with the details of your store.

{% endif %}

When using your Dedicated Snap Store, your main resource will be the documentation found in the `Dedicated Snap Store documentation <https://documentation.ubuntu.com/dedicated-snap-store/>`_.
This section provides links to some key pages in the documentation, as well as information specific to your Dedicated Snap Store.

Store architecture
------------------

A Snap Store is a repository for hosting and publishing snaps so that they can be consumed by snapd-enabled devices.

There are several Snap Store instances that will be relevant to you. To understand these instances, and the relationship between them, please read:

- `Global Snap Store vs Dedicated Snap Store <https://documentation.ubuntu.com/dedicated-snap-store/explanation/snap-store-vs-dedicated-snap-stores/>`_
- `Base Stores and Device View Stores <https://documentation.ubuntu.com/dedicated-snap-store/explanation/base-stores-and-device-view-stores/>`_

Your Base Snap Store is:  ``{{CUSTOMER_STORE_NAME}}`` (``{{CUSTOMER_STORE_ID}}``)

Your Device View Snap Store is: ``{{CUSTOMER_DEVICEVIEW_NAME}}`` (``{{CUSTOMER_DEVICEVIEW_ID}}``)

Your Device View Store is configured:

- to automatically include all snaps from ``{{STORES_WITH_WHOLESALE_INCLUSION}}``
- to include a specific set of snaps from ``{{STORES_WITH_CURATED_INCLUSION}}``

All stores (including your Device View Snap Store) always include the snapd snap, as well as the LTS-versioned Core snaps (i.e. core18, core20, core22, core24).

.. note::

   If and when your organization decides to create additional models, please ensure that you first request and use a new Device View Store for each new model. This can be done by opening a support ticket via your support portal. Using a single Device View Store per model allows for better isolation between your various models and ensures that potential changes to the inclusion rules for one model don't impact other models which may already be in use in production.

Accounts and roles
------------------

Ubuntu SSO accounts underpin developer interactions with the various Stores. To understand accounts and roles, please read:

* `Ubuntu SSO Accounts <https://documentation.ubuntu.com/dedicated-snap-store/explanation/ubuntu-sso-accounts/>`_
* Users and Roles:
    * `Administrator <https://documentation.ubuntu.com/dedicated-snap-store/how-to/setting-up-account-roles/#account-roles>`_
    * `Reviewer <https://documentation.ubuntu.com/dedicated-snap-store/how-to/setting-up-account-roles/#account-roles>`_
    * `Viewer <https://documentation.ubuntu.com/dedicated-snap-store/how-to/setting-up-account-roles/#account-roles>`_
    * `Publisher <https://documentation.ubuntu.com/dedicated-snap-store/how-to/setting-up-account-roles/#account-roles>`_
    * `Collaborator <https://documentation.ubuntu.com/dedicated-snap-store/how-to/setting-up-account-roles/#account-roles>`_

Your store has been provisioned with the following data:

.. list-table::
   :widths: 20 40 40
   :header-rows: 1
   :stub-columns: 1

   * -
     - Base Store
     - Device view Store
   * - Store Name
     - {{CUSTOMER_STORE_NAME}}
     - {{CUSTOMER_DEVICEVIEW_NAME}}
   * - Store ID
     - {{CUSTOMER_STORE_ID}}
     - {{CUSTOMER_DEVICEVIEW_ID}}
   * - Admin(s)
     - {{CUSTOMER_ADMIN_EMAIL}}
     - {{CUSTOMER_ADMIN_EMAIL}}
   * - Publisher(s)
     - {{CUSTOMER_BRAND_EMAIL}}
     - (none)
   * - Reviewer(s)
     - {{CUSTOMER_ADMIN_EMAIL}}
     - (none)
   * - Viewer(s)
     - {{CUSTOMER_VIEWER_EMAIL}}
     - {{CUSTOMER_VIEWER_EMAIL}}

The Admin role can be used to grant these roles to other accounts, as well.

Brand account
-------------

Account: ``{{CUSTOMER_BRAND_EMAIL}}`` (account-id: ``{{CUSTOMER_BRAND_ACCOUNT_ID}}``)

The Brand account was set up for your Dedicated Snap Stores at the time of store creation.  The Brand account defines the Brand scope of authority, and it must be used for certain functions.

The Brand account:

- Uses Serial Vault to generate or register signing keys for use with Brand infrastructure.
- Signs Model assertions used to build images that point at Dedicated Snap Stores.
- Signs System-User assertions used to trigger user-account creation on Brand devices.
- Publishes any gadget snaps in the store. Kernel and gadget snap names must be owned by the Brand account or by Canonical. Typically, Canonical owns kernels, and the Brand account owns gadget snaps. To do this, the Brand account must be given the **Publisher** role in the Base store.

  * After registering the names, the Brand account may make other developer accounts **Collaborators** on these snaps. These accounts then may upload future revisions of these snaps.

.. note::

  Use of the Brand account and its credentials should be strictly limited. Canonical recommends that the Brand account not be assigned any roles that are not strictly needed. The Brand account will need the **Publisher** role, but do not make the Brand account a store **Administrator**, **Reviewer**, or **Viewer**. After registering snap names, the Brand account may make other developer accounts **Collaborators** on these snaps. These accounts then may upload future revisions of these snaps. Using collaborators instead of the Brand account to publish snaps is encouraged, as this further reduces use of the Brand account. 

.. important::

    It is recommended to generate keys using hardware security modules.

Brand keys
**********

Ubuntu Core relies on a number of signed documents called `assertions <https://snapcraft.io/docs/assertions>`_, of which there are multiple types. Some of these assertions are signed by Canonical, and some must be signed by keys controlled by the Brand Account. This section discusses some best practices that you are strongly suggested to follow.

1. Please be sure to review the `signing keys sub-section <https://canonical-serial-vault.readthedocs-hosted.com/serial-vault/signing-keys/>`_ on key roles. Use of key roles is a best practice which helps to limit the type of assertions each key can be used to sign. This is meant to limit your exposure if a key were to be compromised. Use of key roles also means that you must no longer register your keys using snapcraft register-key. This will now be handled by the Snap Store admins as part of the key role assignment. And finally, please note that key roles can only be assigned to new keys, they cannot be added to keys after registration.

2. Limit access to brand keys. It's strongly advised that you consider using a PKI system or key vault to protect your brand keys, and limit access to them. Hardware cryptotokens are another possibility, although they may be more challenging to use than PKI systems in practice.

3. For signing Serial assertions, please use the Serial Vault's "generate key" facility instead of creating a local key and importing it.



Ubuntu Pro & Support Portal account
-----------------------------------

An Ubuntu Pro account and Support Portal access are also included with your Dedicated Snap Store. Both are accessed using the SSO account associated with the following email address:

    {{CUSTOMER_PRO_EMAIL}}


Ubuntu Pro Dashboard
********************

Dedicated Snap Store customers are provided an Ubuntu Pro account to enable access to ESM updates during snap builds (enabled by use of the `SNAPCRAFT_UA_TOKEN`). This is accomplished by adding your Pro token to CI/CD systems used to build your snaps. This token can be accessed by signing into the `Ubuntu Pro Dashboard <http://ubuntu.com/pro/dashboard>`_ using the account mentioned at the beginning of this section.

Support Portal
**************

Dedicated Snap Store customers are also provided access to our Support Portal which can be used to create support cases, including `requests for super privileged interface connections <https://snapcraft.io/docs/super-privileged-interfaces>`_. The support portal can be accessed by signing into the `Support Portal Dashboard <https://support-portal.canonical.com/dashboard>`_ using the account mentioned at the beginning of this section. 

Interface connection cases
**************************

Please provide the following basic information when submitting a snap interface connection request support case:

* Snap Name
* Snap ID
* Snap Interface (e.g. network-control)
* ID of any other snaps involved
* [Optional] Required Snap Interface slots
* Description of why this interface is needed.

Landscape
---------

Landscape is a new feature in Ubuntu Core 24. It enables customers to manage a fleet of devices, control updates, trigger remote snap installs, and other more advanced fleet management features. 

 
Landscape is made available to Ubuntu Core customers through a software-as-a-service (SaaS) model, hosted and managed by Canonical. 

 
Please contact customersuccess@canonical.com to request a Landscape SaaS account. 

Self-hosted Landscape 
*********************

Alternatively, Landscape Server can run on-premises or in public clouds. The `Landscape Server quickstart <https://ubuntu.com/landscape/docs/quickstart-deployment>`_ installation guide is the fastest way to get started, but other installation options for Landscape Server are available in the Landscape documentation. 

Serial Vault
------------

Serial Vault has been provisioned with an account for ``{{CUSTOMER_ADMIN_EMAIL}}``, allowing this account to log into the Serial Vault for administrative purposes, including making configurations required for device authentication against a Dedicated Snap Store, as described in :doc:`/how-to/configure-serial-vault`. 

.. only:: html
    
    To configure Serial Vault, see :doc:`/how-to/configure-serial-vault`.