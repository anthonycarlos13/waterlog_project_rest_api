__author__ = 'anthonymendoza'

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.apps import apps
from django.db.models import Q
from water_store.serializers import CountrySerializer, StateSerializer, CountySerializer
from helpers.location_helpers import import_data_to_data_models

from helpers.ground_water_data_aggregator import ground_water_helper
from helpers.precipitation_data_aggregator import precipitation_water_helper

county_model = apps.get_model('water_store', 'County')


@api_view(['GET'])
def county_api(request, format=None, **kwargs):
    if request.method == 'GET':
        county = kwargs['county']
        state = kwargs['state']

        if str.lower(str(county)) == 'all':
            _county_existence_check = county_model.objects.filter(state_internal__abbreviation__iexact=state)
            county_serializer = CountySerializer(_county_existence_check, many=True)

        else:
            _county_existence_check = county_model.objects.filter(Q(state_internal__abbreviation__iexact=state),Q(county_code=county))
            county_serializer = CountySerializer(_county_existence_check, many=True)

        return Response(county_serializer.data, status.HTTP_200_OK)
    else:
        return Response(exception=ValueError("This REST API only supports 'GET' requests"))
