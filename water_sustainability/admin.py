from django.contrib import admin
from django.apps import apps


storm_water_model_instance = apps.get_model('water_sustainability', 'StormWater')
admin.site.register(storm_water_model_instance)


# class StormWaterAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Name',
#          {'fields': ['year', 'total_annual_rainfall', 'total_annual_rainfall_units', 'annual_change_from_previous_year',
#                      'annual_change_from_average', 'amount_annual_capture', 'amount_annual_capture_units',
#                      'amount_annual_capture_units', 'total_capture_per_annum', 'main_source']}),
#     ]