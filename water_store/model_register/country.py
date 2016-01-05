__author__ = 'anthonymendoza'

from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    abbreviation = models.CharField(max_length=5, null=True, blank=True)
    country_code = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("name", "abbreviation")

