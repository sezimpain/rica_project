from django import forms
from django.forms import widgets
from .models import school_type_choices

from django.db import models

class StudentForm(forms.Form):
    name_and_family = forms.CharField(max_length=300, required=True, label="Имя и фамилия")
    date = forms.DateField(required=True, label='Дата рождения')
    phone_number = forms.CharField(max_length=20, required=True, label="Мобильный номер")
    school_type = forms.ChoiceField(choices=school_type_choices, required=True, label="Учится в ")
    grade = forms.CharField(required=True, label="Класс")
    pay = forms.CharField(required=True, label="Плата за обучение")
    registered = forms.CharField(required=True, label="Зарегестрировал")
    address = forms.CharField(required=True, label="Домашний адрес")
    extra_classes = forms.CharField(required=True, label="Кружки")
    additional_info = forms.CharField(required=True, label="Примечания")

    father_name = forms.CharField(required=True, label="Имя и фамилия отца")
    father_phone = forms.CharField(required=True, label="Контакты отца")
    father_job = forms.CharField(required=True, label="Работа отца")

    mother_name = forms.CharField(required=True, label = "Имя и фамилия матери")
    mother_phone = forms.CharField(required=True, label="Контакты матери")
    mother_job = forms.CharField(required=True, label="Работа матери")
