__author__ = 'anthonymendoza'

from rest_framework import serializers
from django.apps import apps


class SpreadingGroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model("water_store", "SpreadingGround")
        fields = ('id', 'site_name', 'latitude',
                  'longitude', 'county',
                  'date', 'area', 'percolation', 'storage', 'units',
                  'source')
        read_only_fields = ['id']