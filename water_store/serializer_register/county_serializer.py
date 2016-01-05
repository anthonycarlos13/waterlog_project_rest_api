__author__ = 'anthonymendoza'

from rest_framework import serializers
from django.apps import apps


class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model("water_store", "County")
        fields = ('id', 'name', 'state_internal', 'county_code',
                  'active_status', 'state_name',
                  'state_abbreviation',
                  'state_code')
        read_only_fields = ['id']