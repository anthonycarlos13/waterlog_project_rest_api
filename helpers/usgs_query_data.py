__author__ = 'anthonymendoza'
import csv
import json
import requests
import xml.etree.ElementTree as ET
from water_sustainability.data_store import county_codes, gw_levels_2014


def retrieve_real_time_ground_water_levels_los_angeles_county_as_json(local_code, start_date, end_date):
    payload = {'format': 'json',
               'countyCd': local_code,
               'startDT': start_date,
               'endDT': end_date}
    url = 'http://waterservices.usgs.gov/nwis/gwlevels'
    response = requests.get(url, params=payload)
    status = response.status_code
    rel_data = json.loads(response.text)
    for key, value in rel_data.iteritems():
        pass


def check_valid_county_code(state_code, county_code):
    county = None
    db = open(county_codes)
    county_data = csv.DictReader(db)

    for data in county_data:
        if str(data['state_cd']) == str(state_code):
            if str(data['county_cd']) == str(county_code):
                county = data['county_nm']

    if county is None:
        raise ValueError("incorrect state or county code")
    return county


def retrieve_real_time_ground_water_levels_los_angeles_county_as_xml(county_code, start_date, end_date):
    processed_data = []
    # if check_valid_county_code(state_code, county_code):
    #     pass
    # else:
    #     raise ValueError("County Code not recognized.")
    #
    # if county_code == '037' and state_code == 'california':
    #     response = gw_levels_2014
    # else:
    payload = {'format': 'waterml',
               'countyCd': county_code,
               'startDT': start_date,
               'endDT': end_date}
    url = 'http://waterservices.usgs.gov/nwis/gwlevels'
    response = requests.get(url, params=payload)
    status = response.status_code
    root = ET.fromstring(response.text)
    if status == 200:
        processed_data = time_series_aggregator(root)
    return processed_data


def time_series_aggregator(root):
    gw_sites_agg_data = []
    for timeSeries in root:
        # Need to reset each pointer with each new timeseries being parsed
        gw_sites_and_measurements = {}
        for child in timeSeries:
            if child.tag == '{http://www.cuahsi.org/waterML/1.2/}sourceInfo':
                if child.find('{http://www.cuahsi.org/waterML/1.2/}siteCode') is None:
                    break
                else:
                    gw_site_code_number = child.find('{http://www.cuahsi.org/waterML/1.2/}siteCode').text
                    gw_sites_and_measurements['site_code'] = gw_site_code_number

            elif child.tag == '{http://www.cuahsi.org/waterML/1.2/}values':
                if child.find('{http://www.cuahsi.org/waterML/1.2/}value') is None:
                    break
                else:
                    gw_date_last_measured = child.find('{http://www.cuahsi.org/waterML/1.2/}value').get('dateTime')
                    gw_site_measurement = child.find('{http://www.cuahsi.org/waterML/1.2/}value').text
                    gw_sites_and_measurements['site_measurement'] = gw_site_measurement
                    gw_sites_and_measurements['date_last_measured'] = gw_date_last_measured

            # Want to keep the pointer alive until the iter obtains values so this ensures no site code is input alone
            if (gw_sites_and_measurements not in gw_sites_agg_data) and (len(gw_sites_and_measurements) > 1):
                gw_sites_agg_data.append(gw_sites_and_measurements)
    return gw_sites_agg_data
