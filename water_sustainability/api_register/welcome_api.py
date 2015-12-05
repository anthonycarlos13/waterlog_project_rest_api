__author__ = 'anthonymendoza'

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def welcome(request, format=None):
    if request.method == 'GET':
        response = "Welcome to the REST API. Please see documentation for usage details." \
                   " If you have questions, contact mendoza.anthony1992@gmail.com"
        return Response(response, status.HTTP_200_OK)
    else:
        return Response(exception=ValueError("Do not post, put, delete to this endpoint. Silly person."))
