from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Checks if users are updating their own profile"""

    def has_object_permission(self, request, view, obj):
        """
        Returns true if request.user's id matches the id of profile being requested for change
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
