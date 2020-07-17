# Create your views here.
import json

from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def home(request):
    """This code is run when we """
    return HttpResponse("Hello World")


def add(request):
    """Adds 2 numbers, coming as num1 and num2 in simple GET Request. After
    Addition, it gives Result in HttpResponse"""
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    return HttpResponse(f"Result {val1+val2}")


@csrf_exempt
def addPost(request):
    """Adds 2 numbers, coming as num1 and num2 in POST Request. The API expects application/json
    content type. After Addition, it gives Result in HttpResponse"""
    request_json = json.loads(request.body)
    val1 = int(request_json["num1"])
    val2 = int(request_json["num2"])

    return HttpResponse(f'Result is: {val1+val2}')
