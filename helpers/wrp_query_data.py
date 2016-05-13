from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from django.apps import apps
import statistics
import csv

from water_store.data_store.los_angeles_county import wrp_data
import helpers.query_helpers

wrp_model = apps.get_model('water_store', 'ReclamationPlant')
county_model = apps.get_model('water_store', 'County')
lac = county_model.objects.get(name__iexact="Los Angeles County", county_code=37)


def wrp_query_helper():
    db = open(wrp_data)
    wrp = csv.DictReader(db)
    for data in wrp:
        name = data['Plant']
        region = data['Region']
        treatment_type = data['Treatment']
        capacity_MGD = data['Capacity']
        water_producedMGD = data['WaterProducedMGD']
        date_recorded = datetime(int(data['Year']), 12, 31)
        water_producedAFY = data['WaterProducedAFY']
        # county = lac
        operation_management_costAFY = data['O&M($/AF)']
        operation_management_costY = data['O&M($/Y)']
        water_reusedMGD = data['Water Reused (MGD)']
        water_reusedAFY = data['Water Reused (AFY)']
        reuse_sites = data['Reuse Sites']
        reuse_sites_sizeACRES = data['Reuse Site Size (Acres)']

        _wrp = wrp_model(name=name, region=region, treatment_type=treatment_type, capacity_MGD=capacity_MGD,
                         water_producedMGD=water_producedMGD, water_producedAFY=water_producedAFY, date_recorded=date_recorded,
                         county=lac, operation_management_costAFY=operation_management_costAFY,
                         operation_management_costY=operation_management_costY,
                         water_reusedMGD=water_producedMGD, water_reusedAFY=water_reusedAFY,
                         reuse_sites=reuse_sites, reuse_sites_sizeACRES=reuse_sites_sizeACRES)
        _wrp.save()
    db.close()
