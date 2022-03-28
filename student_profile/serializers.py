from rest_framework.serializers import ModelSerializer

from rica_project.student_profile.models import Student


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

