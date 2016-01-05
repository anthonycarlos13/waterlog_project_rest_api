__author__ = 'anthonymendoza'

from rest_framework import serializers
from django.apps import apps


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model("water_store", "State")
        fields = ('id', 'name', 'country_internal', 'state_code',
                  'country_name', 'country_code',
                  )
        read_only_fields = ['id']