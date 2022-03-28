from rest_framework.permissions import BasePermission


class IsOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        print("PERMISSION: ", request.user, obj.owner )
        return bool(
            request.user == obj.owner
        )


