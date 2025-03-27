Control updates
===============

One important consideration when deploying devices running Ubuntu Core is determining how to control updates, in particular when those updates are for snaps from other publishers (e.g. Canonical). There are three general approaches to controlling and/or gating snap updates on Ubuntu Core:

* `Refresh Control <https://ubuntu.com/core/docs/refresh-control>`_ - this method provides a way to hold one or more snaps at specific revisions until newer revisions have first been validated by the brand. It can be enabled by opening a support ticket and requires a special gating snap which must be included in your images.

* `Validation Sets <https://snapcraft.io/docs/validation-sets>`_ - this method provides a similar mechanism to Refresh Control, however it's based on a special type of assertion called a validation-set. These assertions can be added at runtime to Ubuntu Core devices or seeded at image creation time by specifying one or more validation-set assertions in your model assertion. One advantage of validation sets vs. Refresh Control is that they allow a set of interrelated snaps to be validated as a set vs. validating snaps one by one.

* **Device Agent** - the final method that can be used to control updates involves use of a device agent, which is a dedicated service that takes full control of updates on an Ubuntu Core system by use of snapd's REST API. For more details, please see the `snapd-control interface <https://snapcraft.io/docs/snapd-control-interface>`_.

.. note::

   While Refresh Control is still supported, Validation Sets provide a more comprehensive approach to controlling updates, and in particular can guarantee that only specific combinations of snap revisions can be installed together.
