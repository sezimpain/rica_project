from django.contrib.contenttypes.fields import GenericRelation
from django.db import models


class School(models.Model):

    city = models.CharField(
        max_length=255,
        null=True,
        blank=True

    )
    number = models.IntegerField(
        null=True,
        blank=True)

    address = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    owner = models.CharField(max_length=255,null=True,blank=True)





