from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.apps import apps
from django.db.models import Q
from helpers.usgs_query_data import retrieve_real_time_ground_water_levels_los_angeles_county_as_xml
from helpers.wrp_query_data import wrp_query_helper
from helpers.cimis_query_data import data_json_cimis
from helpers.sp_ground_data import sp_gds_gimme
from helpers.usgs_add_query import retrieve_los_angeles_county_as_xml
from water_store.serializer_register import GroundWaterWellSerializer
from water_store.serializer_register import ReclamationPlantSerializer, StreamSerializer, PrecipitationSerializer, SpreadingGroundSerializer, EvapotranspirationSerializer

groundwater_model = apps.get_model('water_store', 'GroundWaterWell')
reclamation_model = apps.get_model('water_store', 'ReclamationPlant')
stream_model = apps.get_model('water_store', 'Stream')
precip_model = apps.get_model('water_store', 'Precipitation')
evapo_model = apps.get_model('water_store', 'Evapotranspiration')
spr_model = apps.get_model('water_store', 'SpreadingGround')


@api_view(['GET'])
def facility_data_api(request, format=None, **kwargs):
    if request.method == 'GET':
        fac = request.query_params['facility']
        if fac == 'groundwater_wells':
            if groundwater_model.objects.filter(county__name__iexact='los angeles county').count() == 0:
                retrieve_real_time_ground_water_levels_los_angeles_county_as_xml()
            gwells = groundwater_model.objects.filter(county__name__iexact="los angeles county")
            _serializer = GroundWaterWellSerializer(gwells, many=True)
        elif fac == "water_reclamation_plants":
            if reclamation_model.objects.filter(county__name__iexact='los angeles county').count() == 0:
                wrp_query_helper()
            wrps = reclamation_model.objects.all()
            _serializer = ReclamationPlantSerializer(wrps, many=True)
        elif fac == 'streams':
            if stream_model.objects.filter(county__name__iexact='los angeles county').count() == 0:
                retrieve_los_angeles_county_as_xml('ST')
            str = stream_model.objects.all()
            _serializer = StreamSerializer(str, many=True)
        elif fac == 'springs':
            return
        elif fac == 'lakes':
            return
        elif fac == 'reservoirs':
            return
        elif fac == 'precipitation':
            if precip_model.objects.filter(county__name__iexact='los angeles county').count() == 0:
                data_json_cimis()
            pre = precip_model.objects.all()
            _serializer = PrecipitationSerializer(pre, many=True)
        elif fac == 'spreading_grounds':
            if spr_model.objects.filter(county__name__iexact='los angeles county').count() == 0:
                sp_gds_gimme()
            spr = spr_model.objects.all()
            _serializer = SpreadingGroundSerializer(spr, many=True)
        elif fac == 'evapotranspiration':
            if evapo_model.objects.filter(county__name__iexact='los angeles county').count() == 0:
                data_json_cimis()
            pre = evapo_model.objects.all()
            _serializer = EvapotranspirationSerializer(pre, many=True)
        elif fac == 'imported_water':
            return
        elif fac == 'conserved_water':
            return
        else:
            return Response("facility type not found!", status=status.HTTP_400_BAD_REQUEST)

        return Response(_serializer.data, status=status.HTTP_200_OK)
