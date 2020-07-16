from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    """This code is run when we """
    return HttpResponse("Hello World")


def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    return HttpResponse(f"Result {val1+val2}")

