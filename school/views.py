from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from school.models import School
from school.serializers import SchoolSerializer
from .permissions import IsOwnerPermission





class PermissionMixin:
    def get_permissions(self):
        print('ACTION: ', self.action)
        if self.action in ['create', 'update', 'partial_update', 'destroy', 'post']:
            permissions = [IsOwnerPermission,IsAdminUser]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]



class SchoolViewSet(PermissionMixin, ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context

