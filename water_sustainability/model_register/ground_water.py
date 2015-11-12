__author__ = 'anthonymendoza'
from django.db import models
import arrow

CURRENT_YEAR = arrow.now().year


class GroundWater(models):
    current_year = CURRENT_YEAR
    total_volume_currently_available = models.IntegerField(default=0)
    total_volume_currently_available_units = models.CharField(max_length=5)
