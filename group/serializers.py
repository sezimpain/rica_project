from rest_framework import serializers
from .models import Group


class GroupSerializer(serializers.ModelSerializer):
    teacher = serializers.ReadOnlyField(source='teacher.username')

    class Meta:
        model = Group
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        return representation

    def create(self, validated_data):
        request = self.context.get('request')
        post = Group.objects.create(director=request.user, **validated_data)
        return post
