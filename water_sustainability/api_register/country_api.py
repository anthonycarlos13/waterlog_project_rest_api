__author__ = 'anthonymendoza'

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from helpers.location_helpers import country_helper, state_helper


@api_view(['GET'])
def country_api(request, format=None, **kwargs):
    if request.method == 'GET':
        country = kwargs['country']
        state_codes = str(request.query_params['state_codes'])

        if state_codes == 'True':
            response_obj = state_helper(country)
        else:
            response_obj = country_helper(country)

        return Response(response_obj, status=status.HTTP_200_OK)

    else:
        return Response(exception=ValueError("This REST API only supports 'GET' requests"))


