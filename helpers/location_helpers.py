__author__ = 'anthonymendoza'

from rest_framework.response import Response
import csv

from water_sustainability.data_store import united_states_of_america


# TODO migrate these to the helpers dir
def country_helper(country):
    data_resp_obj = {}

    if str(country).lower() in ['000', 'usa', 'us', 'united_states', 'united_states_of_america']:
        db = open(united_states_of_america.county_codes)
        county_codes = csv.DictReader(db)
        # State = namedtuple("State", ["state", "state_code"])

        for data in county_codes:
            current_state = data['state']

            if current_state not in data_resp_obj:
                data_resp_obj[current_state] = [{'county': data['county'],
                                             'county_code': data['state_code']+data['county_code'],
                                             'active_status': data['active_status']}]
            else:
                data_resp_obj[current_state].append(
                    {'county': data['county'],'county_code': data['state_code']+data['county_code'],'active_status': data['active_status']})
        error = None

    else:
        error = Response(exception=ValueError("We do not support your country"))

    response_obj = {
            'notes': "analytics for entire state coming soon",
            'source': "United States Census Bureau",
            'source_url': "http://www.census.gov/2010census/partners/pdf/FIPS_StateCounty_Code.pdf",
            'data': data_resp_obj,
            'error_message' : error
        }

    return response_obj


def state_helper(country):
    data_resp_obj = {}

    if str(country).lower() in ['000', 'usa', 'us', 'united_states', 'united_states_of_america']:
        db = open(united_states_of_america.county_codes)
        county_codes = csv.DictReader(db)
        # State = namedtuple("State", ["state", "state_code"])

        for data in county_codes:
            current_state = data['state']

            if current_state not in data_resp_obj:
                data_resp_obj[current_state] = data['state_code']
            else:
                data_resp_obj[current_state] = data['state_code']

        error = None

    else:
        error = Response(exception=ValueError("We do not support your country"))

    response_obj = {
            'notes': "analytics for entire state coming soon",
            'source': "United States Census Bureau",
            'source_url': "http://www.census.gov/2010census/partners/pdf/FIPS_StateCounty_Code.pdf",
            'data': data_resp_obj,
            'error_message' : error
    }

    return response_obj


def county_helper(country, state):
    state_data = []
    if str(country).lower() in ['000', 'usa', 'us', 'united_states', 'united_states_of_america']:
        _county_helper_response = country_helper(country=country)

        if _county_helper_response['error_message'] is None:
            try:
                state = str(state).upper()
                state_data = _county_helper_response['data'][state]
                error_message = None
            except Exception as e:
                error_message = "%s" % e
        else:
            error_message = _county_helper_response['error_message']

        response_obj = {
            'notes': "Analytics for country coming soon",
            'source': "United States Census Bureau",
            'source_url': "http://www.census.gov/2010census/partners/pdf/FIPS_StateCounty_Code.pdf",
            state: state_data,
            'error_message': error_message
        }

        return response_obj

