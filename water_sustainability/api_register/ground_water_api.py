__author__ = 'anthonymendoza'

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.apps import apps
import statistics
from django.db.models import Q
import csv

from water_sustainability.serializers import StormWaterSerializer
from water_sustainability.data_store.los_angeles_county_data_store import well_depth_data
import helpers.usgs_query_data

CALIFORNIA_STATE_CODE = '06'
LOS_ANGELES_COUNTY_CODE = '06037'
FORMAT_DATA = 'json'
START_DATE = '2014-01-01'
END_DATE = '2015-01-01'


@api_view(['GET'])
def ground_water_api(request, format=None):
    if request.method == 'GET':
        if request.query_params['method'] == 'ground_water_wells':
            if request.query_params['raw_data'] == 'true':
                response = []
                _gw_data = helpers.usgs_query_data.retrieve_real_time_ground_water_levels_los_angeles_county_as_xml(
                    county_code=LOS_ANGELES_COUNTY_CODE,
                    start_date=START_DATE,
                    end_date=END_DATE
                )
                _well_data = {}
                db = open(well_depth_data)
                well_depths = csv.DictReader(db)

                for data in well_depths:
                    _well_data[data['site']] = data['well_depth']

                for site_data in _gw_data:
                    if site_data['site_code'] in _well_data.keys():
                        site_data['well_depth'] = _well_data[site_data['site_code']]
                    else:
                        site_data['well_depth'] = 'WELL IS NOT ACTIVE'
                print _gw_data
                response.append(_gw_data)
                return Response(response, status=status.HTTP_200_OK)
            # elif request.query_params['raw_data'] == 'false':
            #     storm_water_model_instance = apps.get_model('water_sustainability', 'StormWater')
            #     storm_water_serializer = StormWaterSerializer
            #     return helpers.query_helpers.get_products(storm_water_model_instance, storm_water_serializer, request)
            else:
                return Response(
                    exception=ValueError("Unrecognized input for raw_data query param. Please use 'true' or 'false'."))
    else:
        return Response(exception=ValueError("We currently do not have data on your method of water sustainability"))
