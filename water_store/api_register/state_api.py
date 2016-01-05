__author__ = 'anthonymendoza'

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.apps import apps
from django.db.models import Q
from water_store.serializers import StateSerializer
from helpers.location_helpers import import_data_to_data_models

state_model = apps.get_model('water_store', 'State')

@api_view(['GET'])
def state_api(request, format=None, **kwargs):
    if request.method == 'GET':
        state = kwargs['state']

        if str.lower(str(state)) == 'all':
            _state_existence_check = state_model.objects.all()
            state_serializer=StateSerializer(_state_existence_check, many=True)
        else:
            _state_existence_check = state_model.objects.filter(Q(abbreviation__iexact=str(state))|
                                                                    Q(name__iexact=str(state)))
            state_serializer=StateSerializer(_state_existence_check, many=True)

        return Response(state_serializer.data, status.HTTP_200_OK)
    else:
        return Response(exception=ValueError("This REST API only supports 'GET' requests"))
