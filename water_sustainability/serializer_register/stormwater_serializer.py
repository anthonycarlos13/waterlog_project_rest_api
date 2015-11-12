__author__ = 'anthonymendoza'
from rest_framework import serializers
from django.apps import apps


class StormWaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model("water_sustainability", "StormWater")
        fields = ('year', 'total_annual_rainfall', 'total_annual_rainfall_units', 'annual_change_from_previous_year',
                  'annual_change_from_average', 'amount_annual_capture', 'amount_annual_capture_units',
                  'amount_annual_capture_units', 'total_capture_per_annum', 'main_source')
        read_only_fields = ['id']
