from rest_framework import serializers

from group.serializers import GroupSerializer
from .models import School


class SchoolSerializer(serializers.ModelSerializer):

    # owner = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = School
        fields = '__all__'


    def create(self, validated_data):
        request = self.context.get('request')
        print(request.user)
        post = School.objects.create(**validated_data)
        return post
