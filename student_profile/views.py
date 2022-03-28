from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from rica_project.student_profile.models import Student
from rica_project.student_profile.serializers import StudentSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_classes = StudentSerializer
