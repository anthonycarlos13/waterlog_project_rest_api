from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import api

urlpatterns = [
	url(r'^rest/?', api.facility_data_api),
    url(r'^county/(?P<county>\w{0,50})/$', api.county_api),
]

urlpatterns = format_suffix_patterns(urlpatterns)
