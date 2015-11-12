from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.apps import apps
from django.db.models import Q


@api_view(['GET'])
def water_api(request, format=None):
    if request.method == 'GET':
        response = {
            "studied_methods" : ['Water Runoff', 'Recycled Waste Water', 'Ground Water' ],
            "associated_query_parameters": {
                'Water Runoff': "storm_water",
                'Recycled Water': "recycled_water",
                'Ground Water': "ground_water"
            }
        }
        return Response(response, status=status.HTTP_200_OK)
    else:
        return Response(exception=ValueError("We currently do not have data on your method of water sustainability"))
