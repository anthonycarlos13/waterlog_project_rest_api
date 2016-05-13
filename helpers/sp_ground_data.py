__author__ = 'anthonymendoza'
import csv
import json
import requests
import xml.etree.ElementTree as ET
from water_store.data_store.los_angeles_county import sp_data
from django.apps import apps
import json

"""
    This helper queries CIMIS data.
"""

# TODO add precip model, evapo model!!! 1/20/16 19:28:39
county_model = apps.get_model('water_store', 'County')
lac = county_model.objects.get(name__iexact="Los Angeles County", county_code=37)
sp_model = apps.get_model('water_store', 'SpreadingGround')


def sp_gds_gimme():
    with open(sp_data) as json_file:
        json_data = json.load(json_file)
    data_model_aggregator(json_data)

def data_model_aggregator(root):
    json_tmp = root
    for data in json_tmp:
        sp = sp_model(site_name=data['site_name'], latitude=data['latitude'], longitude=data['longitude'], county=lac, date=data['date'], area=data['area'],
            percolation=data['percolation'], storage=data['storage'], units=data['units'], source=data['source'])
        sp.save()
