__author__ = 'anthonymendoza'

from django.db import models
from county import County


class GroundWaterWell(models.Model):
    site_code = models.CharField(max_length=100, null=True, blank=False)
    latitude = models.DecimalField(decimal_places=2, null=True, blank=False)
    longitude = models.DecimalField(decimal_places=2, null=True, blank=False)
    county = models.ForeignKey(County, null=True, blank=False)
    date_last_updated = models.DateTimeField(auto_now=True, blank=False, null=True)
    start_date = models.DateTimeField(auto_now=False, blank=False, null=True)
    end_date = models.DateTimeField(auto_now=False, blank=False, null=True)
    date_requested = models.DateTimeField(auto_now=True, null=True, blank=False)
    active = models.BooleanField(null=True, blank=False)

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
        unique_together = ("site_code", "county")

