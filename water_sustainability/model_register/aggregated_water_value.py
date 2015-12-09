__author__ = 'anthonymendoza'

from jsonfield import JSONField
from django.db import models


class AggregatedWaterValue(models.Model):

    sources_dict = {
        'source' : models.CharField(max_length=500, null=False, blank=False),
        'source_url' : models.URLField(null=False, blank=False),
        'source_2': models.CharField(max_length=500, blank=True, null=True),
        'source_2_url' : models.URLField(null=False, blank=False),
    }

    volume = models.IntegerField(default=0, null=False, blank=False)
    volume_units = models.CharField(max_length=5, null=False, blank=False)
    date_requested = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(auto_now=False)
    end_date = models.DateTimeField(auto_now=False)
    location = models.CharField(max_length=500, null=False, blank=False)
    sources_list = JSONField(default=sources_dict)
    total_demand = models.IntegerField(default=0, null=False, blank=False)
