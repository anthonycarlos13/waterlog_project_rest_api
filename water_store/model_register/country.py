__author__ = 'anthonymendoza'

from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    abbreviation = models.CharField(max_length=5, null=True, blank=True)
    continent = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.name

