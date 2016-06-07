from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import api

# TODO [05/31/16]: right now I'll replace the rest endpoint with the reservoir api but ill change it later i guess...
urlpatterns = [
    url(r'^rest/?', api.reservoir_api),
    url(r'^county/(?P<county>\w{0,50})/$', api.county_api),
]

urlpatterns = format_suffix_patterns(urlpatterns)
