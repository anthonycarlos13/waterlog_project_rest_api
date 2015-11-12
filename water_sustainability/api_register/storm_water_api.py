from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.apps import apps
from django.db.models import Q
import csv

from water_sustainability.serializers import StormWaterSerializer
from water_sustainability.data_store.los_angeles_county_data_store import la_county_precipitation_data
import helpers.query_helpers


@api_view(['GET'])
def storm_water_api(request, format=None):
    if request.method == 'GET':
        if request.query_params['method'] == 'storm_water':
            if request.query_params['raw_data'] == 'true':
                data_response = []
                response = {}
                db = open(la_county_precipitation_data)
                precipitation_data = csv.DictReader(db)
                for data in precipitation_data:
                    data_response.append(data)
                db.close()
                response['data'] = data_response
                response['source'] = 'National Weather Service'
                return Response(response, status=status.HTTP_200_OK)
            elif request.query_params['raw_data'] == 'false':
                storm_water_model_instance = apps.get_model('water_sustainability', 'StormWater')
                storm_water_serializer = StormWaterSerializer
                return helpers.query_helpers.get_products(storm_water_model_instance, storm_water_serializer, request)
            else:
                return Response(exception=ValueError("Unrecognized input for raw_data query param. Please use 'true' or 'false'."))
    else:
        return Response(exception=ValueError("We currently do not have data on your method of water sustainability"))
