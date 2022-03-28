from rest_framework import serializers

from group.serializers import GroupSerializer
from .models import School


class SchoolSerializer(serializers.ModelSerializer):
    director = serializers.ReadOnlyField(source='director.username')

    class Meta:
        model = School
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        action = self.context.get('action')
        if action == 'list':
            # representation['students'] = instance.students.count()
            # representation['teachers'] = instance.teachers.count()
            representation['groups'] = instance.groups.count()
        elif action == 'retrieve':
            # representation['students'] = StudentSerializer(
            #     instance.students.all(),
            #     many=True
            # ).data
            # representation['students'] = TeacherSerializer(
            #     instance.teachers.all(),
            #     many=True
            # ).data
            representation['groups'] = GroupSerializer(
                instance.groups.all(),
                many=True
            ).data
        return representation

    def create(self, validated_data):
        request = self.context.get('request')
        post = School.objects.create(director=request.user, **validated_data)
        return post
