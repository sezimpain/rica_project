from django.db import models


class Student(models.Model):
    full_name = models.CharField(max_length=300, verbose_name="ФИО")
    date_of_birth = models.CharField(max_length=150, verbose_name="Дата рождения")
    classroom = models.IntegerField(default=1, verbose_name="Класс")
    address = models.CharField(max_length=400, verbose_name="Адрес проживание")
    additional_info = models.CharField(max_length=500, verbose_name="Доп. информация")
    gender = models.CharField(max_length=150, verbose_name="Пол студента")
    img = models.ImageField(upload_to='images', null=True)
    phone_number = models.CharField(max_length=100, verbose_name="Номер телефона")
    father_full_name = models.CharField(max_length=300, verbose_name="ФИО папы")
    mather_full_name = models.CharField(max_length=300, verbose_name="ФИО папы")

    def __str__(self):
        return self.full_name







