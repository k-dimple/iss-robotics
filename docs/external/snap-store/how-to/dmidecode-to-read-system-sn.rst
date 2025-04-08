Use dmidecode to read system serial number
------------------------------------------

{% if 'admin@acme.com' in CUSTOMER_ADMIN_EMAIL %}
.. warning:: 

  Example values are provided for store configuration in this document. If you are a Dedicated Snap Store customer, you will be provided with a set of documentation with the details of your store.

{% endif %}

One possible approach to populating the serial number (vs. using the ``date`` command) is to use the ``dmidecode`` tool to read the system serial number from the DMI table. In order to do this, you would need to add ``dmidecode`` to that gadget's ``snapcraft.yaml`` file as a ``stage-package``:

.. code:: yaml

    parts:
      prepare-device:
        plugin: nil
        stage-packages:
          - dmidecode
    ...

Also, in ``snapcraft.yaml``, you will need to plug the snapd ``hardware-observe`` interface to allow ``dmidecode`` access to access the correct file(s) in sysfs.

.. note::

    ``hardware-observe`` is a "self-serve interface"; see `Self-serve Snap Interfaces <https://dashboard.snapcraft.io/docs/brandstores/self-serve-interfaces.html>`_ for more details.

.. code:: yaml

    hooks:
      prepare-device:
        plugs: [hardware-observe]
    ...

The actual command to read the serial number will also need to be updated in the snap/hooks/prepare-device file:

.. code:: yaml

    ...
          product_serial=\$(dmidecode -s system-serial-number)
    ...

Finally, to let the hardware-observe interface automatically connect on first boot, you'll need to go to the `dashboard <https://dashboard.snapcraft.io/snaps/{{CUSTOMER_STORE_PREFIX}}-pc/>`_, click on the “Review capabilities” link, and set the radio button next to hardware-observe to “Enabled”.
