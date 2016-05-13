__author__ = 'anthonymendoza'

from rest_framework import serializers
from django.apps import apps


class ReclamationPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model("water_store", "ReclamationPlant")
        fields = ('id', 'name', 'region', 'treatment_type', 'capacity_MGD', 'water_producedMGD', 'date_recorded',
                  'water_producedAFY', 'county',
                  'operation_management_costAFY', 'operation_management_costY', 'water_reusedMGD',
                  'water_reusedAFY', 'reuse_sites', 'reuse_sites_sizeACRES')
        read_only_fields = ['id']