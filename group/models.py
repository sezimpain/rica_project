from django.db import models


class Group(models.Model):

    number = models.IntegerField(
        null=True,
        blank=True)
    name = models.CharField(
        max_length=1,
        null=True,
        blank=True)

    def create_activation_code(self):
        from django.utils.crypto import get_random_string
        code = get_random_string(
            length=8,
            allowed_chars='1234567890qwertyuiop'
        )
        self.activation_code = code

