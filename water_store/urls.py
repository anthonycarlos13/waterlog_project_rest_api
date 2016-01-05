from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import api

urlpatterns = [
    url(r'^(?P<country>\w{0,50})/$', api.country_api),
    url(r'^(?P<country>\w{0,50})/(?P<state>\w{0,50})/$', api.state_api),
    url(r'^(?P<country>\w{0,50})/(?P<state>\w{0,50})/(?P<county>\w{0,50})/$', api.county_api)
]

urlpatterns = format_suffix_patterns(urlpatterns)
