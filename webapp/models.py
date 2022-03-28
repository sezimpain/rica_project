from django.db import models

from account.models import User

school_type_choices = [('elementary', 'Начальная школа'), ('middle', 'Средняя школа'), ('high', 'Старшая школа')]


class Student(models.Model):
    name_and_family = models.TextField(max_length=300, null=False)
    date = models.DateField(null=True, default=None, verbose_name='Дата')
    phone_number = models.CharField(max_length=20)
    school_type = models.CharField(max_length=50, null=False, default='elementary', choices=school_type_choices)
    grade = models.PositiveSmallIntegerField()
    pay = models.CharField(max_length=20)
    registered = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    extra_classes = models.CharField(max_length=500)
    additional_info = models.CharField(max_length=500)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', editable=False, null=True)

    father_name = models.TextField(max_length=300)
    father_phone = models.CharField(max_length=20)
    father_job = models.CharField(max_length=50)

    mother_name = models.TextField(max_length=300)
    mother_phone = models.CharField(max_length=20)
    mother_job = models.CharField(max_length=50)
