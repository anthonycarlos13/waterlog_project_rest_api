__author__ = 'anthonymendoza'

from django.db import models
from django.apps import apps
from country import Country


class State(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    abbreviation = models.CharField(max_length=10, null=True, blank=True)
    country_internal = models.ForeignKey(Country, null=True, blank=True)
    state_code = models.IntegerField(default=0)

    @property
    def country_name(self):
        if self.country_internal is None:
            return None
        return self.country_internal.name

    @property
    def country_code(self):
        if self.country_internal is None:
            return None
        return self.country_internal.country_code

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("name", "abbreviation")
