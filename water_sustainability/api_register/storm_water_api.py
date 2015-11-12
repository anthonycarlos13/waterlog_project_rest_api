from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.apps import apps
import statistics
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
                count = 0
                total_rainfall = 0
                stddev = []
                data_response = []
                min_year = 0
                max_year = 0
                min_rainfall = 100
                max_rainfall = 0
                response = {}
                db = open(la_county_precipitation_data)
                precipitation_data = csv.DictReader(db)
                for data in precipitation_data:
                    count += 1
                    total_rainfall += float(data['Total_Rainfall'])
                    stddev.append(float(data['Total_Rainfall']))
                    if float(data['Total_Rainfall']) > max_rainfall:
                        max_rainfall = float(data['Total_Rainfall'])
                        max_year = data['Season']
                    if float(data['Total_Rainfall']) < min_rainfall:
                        min_rainfall = float(data['Total_Rainfall'])
                        min_year = data['Season']
                    data_response.append(data)
                db.close()
                response['minimum'] = {'min_precipitation': min_rainfall, 'min_year': min_year}
                response['maximum'] = {'max_precipitation': max_rainfall, 'max_year': max_year}
                response['standard_deviation'] = statistics.stdev(stddev)
                response['average_precipitation'] = (float(total_rainfall) / count)
                response['total_precipitation'] = total_rainfall
                response['la_precipitation_per_annum'] = data_response
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
