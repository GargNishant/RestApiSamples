# This is a permission file. The main function is to authenticate the user before they can edit the user profile
# If the user does not have permission, then they will be restricted to make changes

from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allows users to edit their own profile"""

    # This method is called every time a request is made. We can use this
    def has_object_permission(self, request, view, obj):
        # TODO: More info in has_object_permission vs has_permission and their usage
        """Check user is trying to edit their own profile"""
        print("request = ", str(request.data),  obj.id)

        if request.method in permissions.SAFE_METHODS:
            return True

        # object that are ipdating matches the authenticated user profile that is added to the authentication of the request
        return obj.id == request.user.id
