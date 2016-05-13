__author__ = 'anthonymendoza'
import csv
import json
import requests
import xml.etree.ElementTree as ET
from water_store.data_store.los_angeles_county import cimis
from django.apps import apps
import json

"""
    This helper queries CIMIS data.
"""

# TODO add precip model, evapo model!!! 1/20/16 19:28:39
county_model = apps.get_model('water_store', 'County')
lac = county_model.objects.get(name__iexact="Los Angeles County", county_code=37)
evap_model = apps.get_model('water_store', 'Evapotranspiration')
prec_model = apps.get_model('water_store', 'Precipitation')


def data_json_cimis():
    processed_data = []
    payload = {'appKey': '291182ab-3417-461c-8025-2e9acc3d8ad6',
               'targets': '133,99,174,159,204,152,78',
               'startDate': '2015-01-01',
               'endDate': '2016-02-08',
               'dataItems': 'day-eto, day-precip'}
    url = 'http://et.water.ca.gov/api/data?'
    headers = {'content-type': 'application/json'}
    response = requests.get(url, params=payload, headers=headers)
    status = response.status_code

    # with open(cimis) as json_file:
    #     json_data = json.load(json_file)
    # data_model_aggregator(json_data)

    if status == 200:
        data_model_aggregator(response.json())


def data_model_aggregator(root):
    _site_name = None
    _site_code = None
    latitude = None
    longitude = None
    date = None
    value = None
    units = None

    json_tmp = root

    station_list = {
        "133" : {'name': 'Glendale Weather Station', 'latitude': '34.200', 'longitude': '-118.232'},
        "99" : {'name': 'Santa Monica Weather Station', 'latitude': '33.300', 'longitude': '-118.291'},
        '174': {'name': 'Long Beach Weather Station', 'latitude': '33.480', 'longitude': '-118.601'},
        '159': {'name': 'Monrovia Weather Station', 'latitude': '34.09', 'longitude': '-117.590'},
        '204': {'name': 'Santa Clarita Weather Station', 'latitude': '34.260', 'longitude': '-118.310'},
        '152': {'name': 'Camarillo Weather Station', 'latitude': '34.140', 'longitude': '-118.590'},
        '78': {'name': 'Pomonoa Weather Station', 'latitude': '33.400', 'longitude': '-117.490'},
    }

    #Can populate two models at the same time since station info has both in the same level...
    for data in json_tmp.iteritems():
        for providers in data:
            if type(providers) == dict:
                provid = providers
                for stuff in provid.iteritems():
                    for pro in stuff:
                        if type(pro) == list:
                            wialf = pro
                            for the_good_shit in wialf:
                                for wut in the_good_shit.iteritems():
                                    if wut[0] == 'Records':
                                        pre_records = wut
                                        for tp in pre_records:
                                            if type(tp) == list:
                                                data = tp
                                                for win in data:
                                                    _site_code = win['Station']
                                                    date = win['Date']
                                                    eto_value = win['DayEto']['Value']
                                                    eto_units = win['DayEto']['Unit']
                                                    prec_value = win['DayPrecip']['Value']
                                                    prec_units = win['DayPrecip']['Unit']
                                                    _site_name = station_list[str(_site_code)]['name']
                                                    latitude = station_list[str(_site_code)]['latitude']
                                                    longitude = station_list[str(_site_code)]['longitude']
                                                    # NEED to first check if the site is not in the data models already
                                                    if _site_name is not None and _site_code is not None and latitude is not None and longitude is not None:
                                                        eto = evap_model(site_name=_site_name, site_code=_site_code, latitude=latitude,
                                                                                longitude=longitude,
                                                                                county=lac, date=date, active=True, value=eto_value, units=eto_units,
                                                                                source="SCS, WSN, CIMIS, water.ca.gov")
                                                        eto.save()
                                                        prec = prec_model(site_name=_site_name, site_code=_site_code, latitude=latitude,
                                                                                longitude=longitude,
                                                                                county=lac, date=date, active=True, value=prec_value, units=prec_units,
                                                                                source="SCS, WSN, CIMIS, water.ca.gov")
                                                        prec.save()
