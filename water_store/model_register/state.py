__author__ = 'anthonymendoza'

from django.db import models
from django.apps import apps


class State(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    country = models.ForeignKey(apps.get_model(app_label='water_store', model_name='Country'), null=True, blank=True)
    country_code = models.IntegerField(default=0)

    def __str__(self):
        return self.name
