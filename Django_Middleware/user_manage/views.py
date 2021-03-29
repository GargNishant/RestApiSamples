from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(http_method_names=['GET'])
def dummy_api(request):
    user = request.user
    return Response(request.user.email)