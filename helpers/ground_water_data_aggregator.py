__author__ = 'anthonymendoza'

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import csv

from water_store.data_store.los_angeles_county import well_depth_data
import helpers.usgs_query_data


# NOTE: This component assumes that each param is valid to this point.
# IS this a good idea? YES.
def ground_water_helper(cc_code, start_date, end_date):
    """
    :param cc_code:
    :param start_date:
    :param end_date:
    :return: response
    """
    response = []
    _gw_data = helpers.usgs_query_data.retrieve_real_time_ground_water_levels_los_angeles_county_as_xml(
        county_code=cc_code,
        start_date=start_date,
        end_date=end_date
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
            site_data['well_depth'] = 'WELL DATA PENDING'
    response.append(_gw_data)
    response.append("United States Geological Survey")

    return response
