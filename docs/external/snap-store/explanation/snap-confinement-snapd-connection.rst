Snap confinement & snapd interface connections
==============================================

Snaps declare plugs for specific snapd `interfaces <https://snapcraft.io/docs/supported-interfaces>`_ in order to gain access to hardware, shared system resources, and other system interfaces that are normally off-limits to strictly confined snaps. These plugs must be connected to corresponding slots defined by core, application, or gadget snaps. There are three ways that these interface connections can happen:

1. Some interfaces, such as network, simply auto-connect (i.e. there's no action necessary to trigger auto-connection).

#. Some interfaces are classified as "`self-serve <https://dashboard.snapcraft.io/docs/brandstores/self-serve-interfaces.html>`_". These interfaces can be auto-connected by an account with the **Reviewer** role using the store's snap dashboard page.

   .. note::

      The **Reviewer** can only do this if they are not the **Publisher** of or a **Collaborator** on the snap in question.

#. A store support portal ticket can be created to request auto-connection for super-privileged interfaces (e.g. snapd-control or system-files). Please work with your Field Engineer when you create your first such ticket, so as to ensure you provide all the required details. At minimum, you should ensure that you provide:

   - snap name and snap ID
   - interface being requested
   - a brief explanation why the interface is needed and its intended usage
  
   If the interface slot being plugged is provided via the gadget snap, please include the name and snap ID of the gadget snap as well. 

.. note::

   As there's some manual review required for these tickets, please file them as early as possible, as requests to expedite these requests are generally frowned upon.
