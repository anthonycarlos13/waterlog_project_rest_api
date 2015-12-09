__author__ = 'anthonymendoza'

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from helpers.location_helpers import county_helper
from helpers.ground_water_data_aggregator import ground_water_helper
from helpers.precipitation_data_aggregator import precipitation_water_helper


@api_view(['GET'])
def county_api(request, format=None, **kwargs):
    data_resp_obj = {}
    error_message = None

    if request.method == 'GET':
        if valid_county_requested(**kwargs):
            pass
        else:
            error_message = 'county not found'

        _query_response = data_aggregated_from_query_params(request.query_params, **kwargs)
        source = _query_response[1]
        _query_data = _query_response[0]

        response_obj = {
            'notes': "Analytics for country coming soon",
            'source': source,
            'data': _query_data,
            'error_message': error_message
        }

        return Response(response_obj, status.HTTP_200_OK)

    else:
        return Response(exception=ValueError("This REST API only supports 'GET' requests"))


def valid_county_requested(**kwargs):
    county_codes = county_helper(country=kwargs['country'], state=kwargs['state'])
    state = str(kwargs['state'])
    flag = False
    _target_county_code = int(kwargs['county'])

    for _county_data in county_codes[state]:
        cc = int(_county_data['county_code'])
        if cc == _target_county_code:
            flag = True
            break
        else:
            flag = False
    return flag


def data_aggregated_from_query_params(query_params, **kwargs):
    county = kwargs['county']
    sd = query_params['start_date']
    ed = query_params['end_date']
    response_data = []

    if query_params['type'] == 'ground_water':
        response_data = ground_water_helper(cc_code=county, start_date=sd, end_date=ed)
    elif query_params['type'] == 'precipitation':
        response_data = precipitation_water_helper(county=county, start_date=sd, end_date=ed)

    return response_data