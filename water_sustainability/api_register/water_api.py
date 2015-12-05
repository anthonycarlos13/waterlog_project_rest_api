from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.apps import apps
from django.db.models import Q


@api_view(['GET'])
def water_api(request, format=None):
    if request.method == 'GET':
        response = {
            "ground_water" : ['groundwater_wells', 'groundwater_basins'],
            "runoff_water" : ['storm_water_runoff'],
            "recycled_water": ['recycled_water']
        }
        return Response(response, status=status.HTTP_200_OK)