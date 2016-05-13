__author__ = 'anthonymendoza'

from django.db import models
from county import County


class Stream(models.Model):
    site_name = models.CharField(max_length=100, null=True, blank=False)
    site_code = models.CharField(max_length=100, null=True, blank=False)
    latitude = models.DecimalField(decimal_places=6, max_digits=75, null=True, blank=False)
    longitude = models.DecimalField(decimal_places=6, max_digits=75, null=True, blank=False)
    county = models.ForeignKey(County, null=True, blank=False)
    # this needs to be thought of as an 'as of' time period...
    date = models.CharField(max_length=50, blank=False, null=True)
    active = models.BooleanField(null=False, blank=False)
    value = models.DecimalField(decimal_places=2, max_digits=18, null=True, blank=False)
    units = models.CharField(max_length=100, null=True, blank=False)
    source = models.CharField(max_length=500, null=True, blank=False)

    @property
    def state(self):
        if self.county is None:
            return None
        return self.county.state_internal.state_name

    @property
    def country(self):
        if self.county is None:
            return None
        return self.county.state_internal.country_internal.name

    class Meta:
        unique_together = ("site_code", "county", "site_name", "date")
