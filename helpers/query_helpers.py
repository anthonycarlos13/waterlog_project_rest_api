__author__ = 'anthonymendoza'
from django.db.models import Q, QuerySet
from rest_framework.response import Response
from rest_framework import status


def dynamic_field_lookups(query_params):
    Qr = None
    for filter_by, filter_value in query_params.iteritems():
        q = Q(**{"%s" % filter_by: filter_value})
        if Qr:
            Qr = Qr & q
        else:
            Qr = q
    return Qr


def type_of_query_param(param, obj_name, filter_by):
    try:
        param = int(param)
        obj_list = obj_name.objects.filter(id=param)
    except ValueError:
        Qr = Q(**{"%s" % filter_by: param})
        obj_list = obj_name.objects.filter(Qr)
    return obj_list


def get_products(obj_name, obj_serializer, request):
    data = obj_name.objects.all()
    serializer = obj_serializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def update(obj_name, obj_serializer, request):
    Qr = dynamic_field_lookups(request.query_params)
    try:
        obj = obj_name.objects.get(Qr)
    except:
        raise ValueError("cannot make a PUT request to multiple products! Filter by 'id' or 'model_number' instead.")
    serializer = obj_serializer(obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete(obj_name, request):
    Qr = dynamic_field_lookups(request.query_params)
    try:
        obj = obj_name.objects.get(Qr)
    except:
        raise ValueError("cannot make a Delete request to multiple products! Filter by 'id' or 'model_number' instead.")
    obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
