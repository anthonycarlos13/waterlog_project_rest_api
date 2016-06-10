__author__ = 'anthonymendoza'
from django.db.models import Q, QuerySet
from rest_framework.response import Response
from rest_framework import status


def dynamic_field_lookups(query_params):
    Qr = None
    for filter_by, filter_value in query_params.iteritems():
        if filter_by == 'dam_id':
            q = Q(**{"%s__iexact" % filter_by: filter_value})
        else:
            q = Q(**{"%s" % filter_by: filter_value})

        if Qr:
            Qr = Qr & q
        else:
            Qr = q
    return Qr


