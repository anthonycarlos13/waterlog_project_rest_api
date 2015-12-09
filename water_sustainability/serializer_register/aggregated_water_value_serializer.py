# __author__ = 'anthonymendoza'
# from rest_framework import serializers
# from django.apps import apps
#
#
# class AggregatedWaterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = apps.get_model("water_sustainability", "AggregatedWaterValue")
#         fields = ('volume', 'volume_units', 'date_requested', 'start_date', 'end_date', 'location',
#                   'sources_list', 'total_demand',)
#         read_only_fields = ['id']
