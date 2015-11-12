__author__ = 'anthonymendoza'
from django.db import models


class StormWater(models.Model):
    year = models.CharField(max_length=4, null=False, blank=False)
    total_annual_rainfall = models.IntegerField(default=0, null=False, blank=False)
    total_annual_rainfall_units = models.CharField(max_length=25, null=False, blank=False)
    annual_change_from_previous_year = models.IntegerField(default=0, null=False, blank=False)
    annual_change_from_average = models.IntegerField(default=0, null=False, blank=False)
    amount_annual_capture = models.IntegerField(default=0, null=False, blank=False)
    amount_annual_capture_units = models.CharField(max_length=5, null=False, blank=False)
    total_capture_per_annum = models.IntegerField(default=0, null=False, blank=False)
    main_source = models.URLField(null=False, blank=False)
