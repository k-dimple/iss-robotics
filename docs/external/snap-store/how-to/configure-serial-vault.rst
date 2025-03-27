Configure Serial Vault
------------------------

.. configure-serial-vault-start

{% if 'admin@acme.com' in CUSTOMER_ADMIN_EMAIL %}
.. warning:: 

  Example values are provided for store configuration in this document. If you are a Dedicated Snap Store customer, you will be provided with a set of documentation with the details of your store.

{% endif %}

To get started with the `Serial Vault <https://serial-vault-admin.canonical.com/>`_ (SV admin account required), read the following pages. You can click the next button in the bottom right corner to move from one to the next.

- `Serial Vault Overview <https://canonical-serial-vault.readthedocs-hosted.com/>`_
- `Device Model and Identity <https://canonical-serial-vault.readthedocs-hosted.com/serial-vault/device-model-and-identity>`_

To configure your serial vault, follow the instructions at the links below, using ``{{CUSTOMER_MODEL_NAME}}`` as the model name, ``{{CUSTOMER_BRAND_EMAIL}}`` as the brand email, and ``{{CUSTOMER_BRAND_ACCOUNT_ID}}`` as the brand ID:

- `Environment Setup <https://canonical-serial-vault.readthedocs-hosted.com/serial-vault/environment-setup>`_
- `Generate a Serial Signing Key <https://canonical-serial-vault.readthedocs-hosted.com/serial-vault/generate-a-serial-signing-key>`_
- `Register a New Device Model Name <https://canonical-serial-vault.readthedocs-hosted.com/serial-vault/register-a-new-device-model-name>`_
- `Generate a Model Signing Key <https://canonical-serial-vault.readthedocs-hosted.com/serial-vault/generate-a-model-signing-key>`_
- `Check the Signing Log <https://canonical-serial-vault.readthedocs-hosted.com/serial-vault/check-the-signing-log>`_

.. note::

    Although it's possible to generate a local serial signing key and upload it to the Serial Vault, a more secure practice is to use the Serial Vault's key generation facility instead. Using this approach reduces the attack surface as the private key is not accessible externally.
