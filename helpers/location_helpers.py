__author__ = 'anthonymendoza'

from rest_framework.response import Response
import csv

from water_store.data_store import united_states_of_america
from django.apps import apps

country_model = apps.get_model('water_store', 'Country')
state_model = apps.get_model('water_store', 'State')
county_model = apps.get_model('water_store', 'County')


def import_data_to_data_models():
    db = open(united_states_of_america.county_codes)
    usa_county_codes = csv.DictReader(db)

    usa = country_model(name="United States of America", abbreviation="USA", country_code=1)
    usa.save()

    for data in usa_county_codes:
        current_state = data['state']
        try:
            current_state_model = state_model.objects.get(abbreviation__iexact=current_state)

            c = county_model(name=data['county'], state_internal=current_state_model, county_code=data['county_code'],
                             active_status=data['active_status'])
            c.save()
        except Exception:
            s = state_model(name=data['name'], abbreviation=data['state'], country_internal=usa, state_code=data['state_code'])
            s.save()
            c = county_model(name=data['county'], state_internal=s, county_code=data['county_code'],
                             active_status=data['active_status'])
            c.save()
