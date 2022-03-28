from rest_framework.permissions import BasePermission


class IsTeacherPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user == obj.username
        )