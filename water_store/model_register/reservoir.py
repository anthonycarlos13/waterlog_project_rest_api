__author__ = 'anthonymendoza'

from django.db import models

"""
    Fields, units explained:
    reservoir_elevation: feet
    storage: AF
    top_conservation_storage: AF
    outflow: CFS
    inflow: CFS
    evaporation: CFS
    full_natural_flow: CFS
    precipitation: inches
    precipitation_accumulated: inches
"""

# TODO: change county to foreign key? maybe.


class Reservoir(models.Model):
    dam_id = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    reservoir_elevation = models.DecimalField(decimal_places=2, max_digits=75, null=True, blank=True)
    reservoir_storage = models.DecimalField(decimal_places=2, max_digits=75, null=True, blank=True)
    reservoir_area = models.DecimalField(decimal_places=2, max_digits=75, null=True, blank=True)
    latitude = models.DecimalField(decimal_places=3, max_digits=75, null=True, blank=True)
    longitude = models.DecimalField(decimal_places=3, max_digits=75, null=True, blank=True)
    county = models.CharField(max_length=100, null=True, blank=True)
    stream = models.CharField(max_length=100, null=True, blank=True)
    storage_capacity = models.DecimalField(decimal_places=2, max_digits=75, null=True, blank=True)
    outflow = models.DecimalField(decimal_places=2, max_digits=75, null=True, blank=True)
    inflow = models.DecimalField(decimal_places=2, max_digits=75, null=True, blank=True)
    precipitation_incremental = models.DecimalField(decimal_places=2, max_digits=75, null=True, blank=True)
    precipitation_accumulated = models.DecimalField(decimal_places=2, max_digits=75, null=True, blank=True)
    date = models.DateTimeField(auto_now=False, blank=True, null=True)
    source = models.CharField(max_length=500, null=True, blank=True)

    # @property
    # def state(self):
    #     if self.county is None:
    #         return None
    #     return self.county.state_internal.state_name
    #
    # @property
    # def country(self):
    #     if self.county is None:
    #         return None
    #     return self.county.state_internal.country_internal.name

    class Meta:
        unique_together = ("id", "date")

