from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import Group
from .permissions import IsTeacherPermission
from .serializers import GroupSerializer


class PermissionMixin:
    def get_permissions(self):
        if self.action == ['create', 'update', 'partial_update', 'destroy']:
            permissions = [IsAdminUser]

        elif self.action == ['update', 'partial_update', 'destroy']:
            permissions = IsTeacherPermission
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]


class GroupViewSet(PermissionMixin, ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context


