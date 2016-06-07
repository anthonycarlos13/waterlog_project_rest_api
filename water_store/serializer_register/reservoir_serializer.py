__author__ = 'anthonymendoza'

from rest_framework import serializers
from django.apps import apps


class ReservoirSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model("water_store", "Reservoir")
        fields = ('dam_id', 'name', 'reservoir_elevation', 'reservoir_area', 'reservoir_storage',
                  'latitude', 'stream', 'storage_capacity', 'outflow', 'inflow',
                  'longitude', 'county', 'precipitation_incremental', 'precipitation_accumulated',
                  'date', 'source')
        read_only_fields = ['id']