__author__ = 'anthonymendoza'

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.apps import apps
from django.db.models import Q
from django.utils import timezone
from helpers.swp_reservoir_scraper import aggregate_scraped_data
from water_store.serializer_register import ReservoirSerializer
from water_store.serializer_register import ReclamationPlantSerializer, StreamSerializer, PrecipitationSerializer, \
    SpreadingGroundSerializer, EvapotranspirationSerializer
from datetime import datetime
from helpers import query_helpers

reservoir_model = apps.get_model('water_store', 'Reservoir')

station_id_inventory = ['ORO', 'CLE', 'LEW', 'WHI', 'ANT',
                        'SHA', 'KES', 'DAV', 'BUL', 'WRS',
                        'ENG', 'FOL', 'UNV', 'LON', 'INV',
                        'BLB', 'NHG', 'CMN', 'PAR', 'DON',
                        'BRD', 'TUL', 'NML', 'HTH', 'CHV',
                        'BUC', 'HID', 'MIL', 'SNL', 'PNF',
                        'TRM', 'SCC', 'ISB', 'STP', 'DNN',
                        'PYM', 'CAS', 'PRR']


@api_view(['GET'])
def reservoir_api(request, format=None, **kwargs):
    if request.method == 'GET':
        dam_id = request.query_params['dam_id']
        try:
            if dam_id.lower() in map(lambda x: x.lower(), station_id_inventory):
                return query(request.query_params)
            raise KeyError("Invalid ID")
        except Exception as e:
            return Response(e.message, status=status.HTTP_400_BAD_REQUEST)


def query(params):
    Qr = query_helpers.dynamic_field_lookups(params)
    reservoirs = reservoir_model.objects.filter(Qr)
    _serializer = ReservoirSerializer(reservoirs, many=True)
    return Response(_serializer.data, status=status.HTTP_200_OK)


# data = aggregate_scraped_data()
# for i in data.values():
#     for j in i:
#         if j['date'] is not None:
#             input_model = reservoir_model(dam_id=str(j['id']),
#                                           name=str(j['name']),
#                                           reservoir_elevation=None if j['reservoir elevation'] is None or j['reservoir elevation']=='--' else float(''.join(y for y in j['reservoir elevation'] if y.isdigit() or y == '.')),
#                                           reservoir_area=j['reservoir_area'] if type(j['reservoir_area']) is float else float(''.join(y for y in j['reservoir_area'] if y.isdigit() or y == '.')),
#                                           reservoir_storage=None if j['reservoir storage'] is None or j['reservoir storage']=='--' or j['reservoir storage']=='' else float(''.join(y for y in j['reservoir storage'] if y.isdigit() or y == '.')),
#                                           latitude=j['latitude'],
#                                           longitude=j['longitude'],
#                                           county=str(j['county']),
#                                           stream=str(j['stream']),
#                                           storage_capacity=None if j['storage_capacity'] is None else float(''.join(y for y in j['storage_capacity'] if y.isdigit() or y == '.')),
#                                           outflow=None if j['outflow'] is None or j['outflow']=='--' or j['outflow']=='' else float(''.join(y for y in j['outflow'] if y.isdigit() or y == '.')),
#                                           inflow=None if j['inflow'] is None or j['inflow']=='--' or j['inflow']=='' else float(''.join(y for y in j['inflow'] if y.isdigit() or y == '.' or y == ',')),
#                                           precipitation_incremental=None if j['precipitation incremental'] is None or j['precipitation incremental']=='--'else float(''.join(y for y in j['precipitation incremental'] if y.isdigit() or y == '.')),
#                                           precipitation_accumulated=None if j['precipitation accumulated'] is None or j['precipitation accumulated']=='--'else float(''.join(y for y in j['precipitation accumulated'] if y.isdigit() or y == '.')),
#                                           date=datetime.strptime(j['date'], '%m/%d/%Y'),
#                                           source="State Water Project")
#             input_model.save()
#         else:
#             continue
