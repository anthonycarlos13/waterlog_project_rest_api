# __author__ = 'anthonymendoza'
#
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.apps import apps
# from django.db.models import Q
# from water_store.serializers import CountrySerializer, StateSerializer, CountySerializer
# from helpers.location_helpers import import_data_to_data_models
# country_model = apps.get_model('water_store', 'Country')
#
# TODO: (05/08/2016) Do not need this now since scope focus is CA State
# @api_view(['GET'])
# def country_api(request, format=None, **kwargs):
#     try:
#         country_model.objects.get(abbreviation__iexact='usa')
#     except Exception:
#         import_data_to_data_models()
#
#     if request.method == 'GET':
#         country = kwargs['country']
#
#         if str.lower(str(country)) == 'all':
#             _country_existence_check = country_model.objects.all()
#             country_serializer=CountrySerializer(_country_existence_check, many=True)
#
#         else:
#             _country_existence_check = country_model.objects.filter(Q(abbreviation__iexact=str(country))|
#                                                                     Q(name__iexact=str(country)))
#             country_serializer=CountrySerializer(_country_existence_check, many=True)
#
#         return Response(country_serializer.data, status.HTTP_200_OK)
#     else:
#         return Response(exception=ValueError("This REST API only supports 'GET' requests"))
#
#
