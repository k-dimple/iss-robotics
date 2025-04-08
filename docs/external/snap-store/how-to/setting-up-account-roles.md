(setting-up-account-roles)=
# Set up account roles

When setting up account roles, the Administrator should add appropriate accounts with roles to your Base store, where all snaps are registered and published. Here is a look at the [dashboard](https://snapcraft.io/admin) screen an Administrator uses to add Ubuntu SSO accounts to a specific Snap Store with various roles.

An Administrator can navigate to the Users and Roles screen as follows:

* https://snapcraft.io/admin
* Find the appropriate store on the (left side) displayed list, and select the Members on the Top bar of the dashboard.
* Under Users and Roles, select Manage users and their roles.

![Snapcraft dashboard](https://lh5.googleusercontent.com/QaGGrfgBUJm5eXSnRwXzSGM12rcOh0qKc_nesD9OJB0p-FVa0F9f2Id-99QZESwui2mYdQp3fRTZBfNcrM7xXTUGcGgQd0a2VPs4A22iFNsBb0XIZcAhTRDGj4cqqFXwaVrmVPeEZUDw7FoE0jA)
![Add new member menu](https://lh5.googleusercontent.com/16PT0FWIPPFLFSn45tpnwG43VcGcwxbAx7Ij6rh3Gwsl-hVP1JbZZXQVCmPBqy6NOS7CA29f0w3OesU496MKpzrg41dsWhKnYSi5UQ9mL5PsLe1I95o5YoFxB77x3TMbe9FMBm6j2-bhxK1uvwA){w=320px}

You should then review and set the following roles for each store:

* Base Store
  * Publisher
  * Admin, Reviewer
  * Viewer
* Device View Store
  * Admin
  * Viewer

The Device View store does not require Publishers or Reviewers since it does not host snaps but is only a mechanism for curating snaps for device groups.

A Device View store should have at least a Viewer account. This is needed when building images that point to the Device View store. A viewer account can download snaps from the store for inclusion into the image.

(account-roles)=
## Account roles

````{tab-set}

```{tab-item} Administrator

The administrator role in the Dedicated Snap Store has the highest level of permissions granted. Administrator permissions include the abilities to:

* Grant other Ubuntu SSO accounts roles in the Dedicated Snap Store
* Allow members of a team to craft snaps, create snap development teams, review snap revisions, and build images
* Manage snap inclusion (which snaps your devices see - see the section titled *Snap inclusion* to find out more)
```

```{tab-item} Reviewer

The reviewer role in the Dedicated Snap Store is linked to the snap review process that a company may choose to implement. Reviewers approve software changes made to snaps before they can be published to the Store, if the administrator has enabled the requirement for reviews in the Store.
```

```{tab-item} Viewer

The viewer role in the Dedicated Snap Store has the fewest permissions granted. Viewers can see and download snaps from their Dedicated Snap Store. Downloaded snaps can be used to build images or perform testing.

Devices connecting to the Dedicated Snap Store do not require a store account with viewer permissions. To find out more about that see [Connecting Devices](#connecting-devices).
```

```{tab-item} Publisher

As the name suggests, the publisher role in the Dedicated Snap Store is linked to publishing snaps to the Store. The publisher role gives the abilities to:

* Register snap names in the Store
* Upload and release specific snap revisions
* Redact the snap listing and metadata
* Configure a team of collaborators.
```

```{tab-item} Collaborator

A collaborator is a store user that can have equal rights over a particular snap as the snap publisher. This means that a collaborator can upload and release snap revisions. Collaborators can collectively contribute to a snap and administer its listing in the store.

While only snap publishers or collaborators can publish a snap revision, team members can collaborate on the source code of a snap that could be built straight from the code’s repository. 

In the Dedicated Snap Store or the [Snap Store](https://snapcraft.io), a collaborator is role specific to a particular snap. This role can not be assigned at the store level as the store administrator cannot define someone as a collaborator. 

The snap publisher can use the [snaps dashboard](https://dashboard.snapcraft.io/snaps) to manage collaborators assigned to a snap.
```
````