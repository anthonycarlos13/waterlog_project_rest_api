from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import api

urlpatterns = [url(r'^water/data/$', api.StormWaterAPI.storm_water_api),]

urlpatterns = format_suffix_patterns(urlpatterns)
