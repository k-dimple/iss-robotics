(dedicated-snap-store-commissioning)=
# Commission a store

<!-- 
Status: Document is unfocused, and not compliant to a specific Diataxis quadrant
Rewrite: Rework into how-to
 -->

Commissioning a Dedicated Snap Store occurs in four steps:

## 1. Create a Dedicated Snap Store

The first step is to create a brand account. A brand account has extensive permissions. It can be used for certain functions, including to:

* Generate, register and hold the signing keys for all associated Dedicated Snap Stores
* Sign configuration files used to build device images with access to the Dedicated Snap Store
* Register key software components hosted in the App Store (kernels and bootloaders)

## 2. Create SSO accounts and assign roles

Dedicated Snap Stores are administered via a dashboard. Ubuntu SSO is the identity provider for the Dedicated Snap Store - each account requires an email address. The Dedicated Snap Store administrators can assign specific roles to users: administrator, reviewer, viewer, publisher, and collaborator. See the following sections of this guide to find out more about each of these roles.

## 3. Configure the serial vault

The serial vault stores various keys and also provides signed configuration files to devices. These keys allow devices to authenticate against Dedicated Snap Stores. At first boot, a device running Ubuntu Core will perform a provisioning step to retrieve a signed configuration file from the serial vault.

The main configuration files that are stored and served by the serial vault are:

|RESOURCE|DESCRIPTION|
| --- | --- |
|Account key|Cryptographic key used to sign assertions|
|[Model assertion](https://ubuntu.com/core/docs/reference/assertions/model)|A statement about the properties of a device model. It contains information needed to create an Ubuntu Core image|
|[Serial assertion](https://ubuntu.com/core/docs/reference/assertions/serial)|A statement binding a device identity with the device public key.|

All of these files are used by the device, serial vault and the Dedicated Snap Store to verify and manage the access to a device.

## 4. Create sub stores

Store Administrators can create derivative Dedicated Snap Stores hierarchically tied to their account. Sub stores can be created for a number of use cases, including:

* Product sub stores: enterprises with a product portfolio can create sub stores associated with different product lines or to specific product models.
* Ecosystem sub stores: enterprises can create stores on behalf of their ecosystem partners. These could be resellers, subsidiaries or business partners.

### Helpful resources

* [Read more about Dedicated Snap Stores](https://ubuntu.com/internet-of-things/appstore)
* [Dedicated Snap Store datasheet](https://assets.ubuntu.com/v1/d6d1d3fc-IoT+App+Store+Datasheet+v3.pdf)
