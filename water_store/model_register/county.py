__author__ = 'anthonymendoza'

from django.db import models
from django.apps import apps
from state import State


class County(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    state_internal = models.ForeignKey(State, null=True, blank=False)
    county_code = models.IntegerField(default=0)
    active_status = models.CharField(max_length=5, null=True, blank=True)

    @property
    def state_name(self):
        if self.state_internal is None:
            return None
        return self.state_internal.name

    @property
    def state_abbreviation(self):
        if self.state_internal is None:
            return None
        return self.state_internal.abbreviation

    @property
    def state_code(self):
        if self.state_internal is None:
            return None
        return self.state_internal.state_code

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("name", "state_internal")