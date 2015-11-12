from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import api

urlpatterns = [url(r'^water/data/$', api.storm_water_api),
               url(r'^water/$', api.water_api),]

urlpatterns = format_suffix_patterns(urlpatterns)
