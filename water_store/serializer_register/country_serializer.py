__author__ = 'anthonymendoza'

from rest_framework import serializers
from django.apps import apps


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model("water_store", "Country")
        fields = ('id', 'name', 'abbreviation', 'country_code')
        read_only_fields = ['id']