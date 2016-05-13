__author__ = 'anthonymendoza'

from django.db import models
from county import County


class ReclamationPlant(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)
    region = models.CharField(max_length=100, null=True, blank=False)
    treatment_type = models.CharField(max_length=100, null=True, blank=False)
    capacity_MGD = models.DecimalField(decimal_places=4, max_digits=75, null=True, blank=False)
    water_producedMGD = models.DecimalField(decimal_places=4, max_digits=75, null=True, blank=False)
    date_recorded = models.DateTimeField(auto_now=False, blank=False, null=True)
    water_producedAFY = models.DecimalField(decimal_places=4, max_digits=75, null=True, blank=False)
    county = models.ForeignKey(County, null=True, blank=False)
    operation_management_costAFY = models.CharField(max_length=20, null=True, blank=False)
    operation_management_costY = models.CharField(max_length=20, null=True, blank=False)
    water_reusedMGD = models.DecimalField(decimal_places=4, max_digits=75, null=True, blank=False)
    water_reusedAFY = models.DecimalField(decimal_places=4, max_digits=75, null=True, blank=False)
    reuse_sites = models.DecimalField(decimal_places=4, max_digits=20, null=True, blank=False)
    reuse_sites_sizeACRES = models.DecimalField(decimal_places=4, max_digits=20, null=True, blank=False)

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

    # class Meta:
    #     unique_together = ("site_code", "county", "site_name")
