__author__ = 'anthonymendoza'
import csv
import json
import requests
import xml.etree.ElementTree as ET
from water_store.data_store import county_codes, gw_levels_2014
from django.apps import apps


"""
    This helper queries USGS groundwater data. PLEASE NOTE: this uses Waterml1, which will be deprecated by USGS as of January 2016
"""

ground_water_model = apps.get_model("water_store", "GroundWaterWell")
county_model = apps.get_model('water_store', 'County')
lac = county_model.objects.get(name__iexact="Los Angeles County", county_code=37)


def retrieve_real_time_ground_water_levels_los_angeles_county_as_xml():
    processed_data = []
    payload = {'format': 'waterml',
               'countyCd': '06037',
               'siteType': 'GW'}

    url = 'http://waterservices.usgs.gov/nwis/gwlevels'
    response = requests.get(url, params=payload)
    status = response.status_code
    print status
    root = ET.fromstring(response.text)
    if status == 200:
        processed_data = data_model_aggregator(root)
    return processed_data


def data_model_aggregator(root):
    for timeSeries in root:
        gw_site_name = None
        gw_site_code = None
        latitude = None
        longitude = None
        date = None
        value = None
        units = None
        if timeSeries.tag == '{http://www.cuahsi.org/waterML/1.2/}queryInfo':
            pass
        else:
            for child in timeSeries:
                if child.tag == '{http://www.cuahsi.org/waterML/1.2/}sourceInfo':
                    gw_site_name = child.find('{http://www.cuahsi.org/waterML/1.2/}siteName').text
                    gw_site_code = child.find('{http://www.cuahsi.org/waterML/1.2/}siteCode').text
                    geo = child.find('{http://www.cuahsi.org/waterML/1.2/}geoLocation')
                    if geo is not None:
                        for g in geo:
                            latitude = g[0].text
                            longitude = g[1].text
                elif child.tag == '{http://www.cuahsi.org/waterML/1.2/}variable':
                    unit = child.find('{http://www.cuahsi.org/waterML/1.2/}unit')
                    if unit is not None:
                        units = unit.find('{http://www.cuahsi.org/waterML/1.2/}unitCode').text
                elif child.tag == '{http://www.cuahsi.org/waterML/1.2/}values':
                    date = child.find('{http://www.cuahsi.org/waterML/1.2/}value').get('dateTime')
                    value = child.find('{http://www.cuahsi.org/waterML/1.2/}value').text
                else:
                    continue


                # NEED to first check if the site is not in the data models already
                if gw_site_name is not None and gw_site_name is not None and latitude is not None and longitude is not None and units is not None and date is not None and value is not None:
                    gw = ground_water_model(site_name=gw_site_name, site_code=gw_site_code, latitude=latitude, longitude=longitude,
                                            county=lac, date=date, active=True, value=value, units=units, source="NWIS-USGS")
                    gw.save()
