# Generated by Django 3.2.7 on 2022-03-28 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='owner',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
