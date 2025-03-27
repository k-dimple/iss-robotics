(base-stores-and-device-view-stores)=
# Base Stores and Device View Stores

<!-- 
Status: Document is unfocused and does not fit into a Diataxis quadrant
Rewrite: Rework into explanation
 -->

Base Stores and Device View Stores are stores that exist within the Snap Store and are provided by Canonical. To explain them more clearly, we have broken down the concepts here:

In the Base (Snap) Store:

* Private snap names can be registered
* Uploaded snap revisions can be published

The Device View (Snap) Stores are visible to connected devices:

* They can include access to selected snaps in the Base store
* They can also include public snaps from the [global Snap Store](http://snapcraft.io/store).
* Thus, you can curate a specific set of Brand and public snaps for each of your device types (known as device models)

There are a few points to note about Base Stores and Device View Stores. Firstly, production images may only point at a Device View Store, never at the Base Store. Secondly, only your devices can download, install, and refresh snaps from your private Snap Store.

Additionally, for image builds, developers can use their SSO credentials to download snaps from the dedicated Snap Store (please see the Switching to a Developer Account section).The authentication method used by devices is described below.

![Illustration of the App Store architecture, demonstrating use of a combination of public and private snaps](/images/store-architecture.png)

*A standard store configuration using a Base and Device store*

Snap stores are represented by the cylinders, with the Device Snap Store is represented by the cylinder with Acme in the top-right. Acme _view store 1_ has been configured to include snaps from the Global snap store and the [Serial Vault](https://canonical-serial-vault.readthedocs-hosted.com/) is used by the company’s devices to authenticate and thereby gain access to private snaps.
