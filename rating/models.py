from django.db import models


class Rating(models.Model):
    rating = models.PositiveSmallIntegerField()
    # username = models.ForeignKey(
    #     'account.User',
    #     related_name='rating',
    #     on_delete=models.CASCADE
    # )
    # school = models.ForeignKey(
    #     'school.School',
    #     related_name='rating',
    #     on_delete=models.CASCADE
    # )
