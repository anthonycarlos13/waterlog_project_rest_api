__author__ = 'anthonymendoza'

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from helpers.location_helpers import county_helper


@api_view(['GET'])
def state_api(request, format=None, **kwargs):
    if request.method == 'GET':
        response_obj = county_helper(country=kwargs['country'], state=kwargs['state'])
        return Response(response_obj, status.HTTP_200_OK)
    else:
        return Response(exception=ValueError("This REST API only supports 'GET' requests"))
