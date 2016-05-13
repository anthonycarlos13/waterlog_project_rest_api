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

stream = apps.get_model("water_store", "Stream")
county_model = apps.get_model('water_store', 'County')
lac = county_model.objects.get(name__iexact="Los Angeles County", county_code=37)


def retrieve_los_angeles_county_as_xml(type):
    processed_data = []
    payload = {'format': 'waterml',
               'countyCd': '06037',
               'siteType': '%s' % type}
    url = 'http://waterservices.usgs.gov/nwis/iv'
    response = requests.get(url, params=payload)
    status = response.status_code
    print status
    root = ET.fromstring(response.text)
    if status == 200:
        processed_data = data_model_aggregator(root)
    return processed_data


def data_model_aggregator(root):
    for timeSeries in root:
        _site_name = None
        _site_code = None
        latitude = None
        longitude = None
        date = None
        value = None
        units = None
        if timeSeries.tag == '{http://www.cuahsi.org/waterML/1.1/}queryInfo':
            pass
        else:
            for child in timeSeries:
                print child
                if child.tag == '{http://www.cuahsi.org/waterML/1.1/}sourceInfo':
                    _site_name = child.find('{http://www.cuahsi.org/waterML/1.1/}siteName').text
                    _site_code = child.find('{http://www.cuahsi.org/waterML/1.1/}siteCode').text
                    geo = child.find('{http://www.cuahsi.org/waterML/1.1/}geoLocation')
                    if geo is not None:
                        for g in geo:
                            latitude = g[0].text
                            longitude = g[1].text
                elif child.tag == '{http://www.cuahsi.org/waterML/1.1/}variable':
                    unit = child.find('{http://www.cuahsi.org/waterML/1.1/}unit')
                    if unit is not None:
                        units = unit.find('{http://www.cuahsi.org/waterML/1.1/}unitCode').text
                elif child.tag == '{http://www.cuahsi.org/waterML/1.1/}values':
                    date = child.find('{http://www.cuahsi.org/waterML/1.1/}value').get('dateTime')
                    value = child.find('{http://www.cuahsi.org/waterML/1.1/}value').text
                else:
                    continue


                # NEED to first check if the site is not in the data models already
                if _site_name is not None and _site_name is not None and latitude is not None and longitude is not None and units is not None and date is not None and value is not None:
                    st = stream(site_name=_site_name, site_code=_site_code, latitude=latitude, longitude=longitude,
                                            county=lac, date=date, active=True, value=value, units=units, source="NWIS-USGS")
                    st.save()
