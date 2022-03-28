from rest_framework import serializers

from group.serializers import GroupSerializer
from .models import School


class SchoolSerializer(serializers.ModelSerializer):

    # owner = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = School
        fields = '__all__'

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     action = self.context.get('action')
    #     if action == 'list':
    #         representation['groups'] = instance.groups.count()
    #     elif action == 'retrieve':
    #         representation['groups'] = GroupSerializer(
    #             instance.groups.all(),
    #             many=True
    #         ).data
    #     return representation

    def create(self, validated_data):
        request = self.context.get('request')
        print(request.user)
        post = School.objects.create(**validated_data)
        return post
