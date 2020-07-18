from django.http import JsonResponse

# Create your views here.
from travel.models import Destination


def index(request):
    dest1 = Destination()
    dest1.id = 1
    dest1.desc = "Description"
    dest1.name = "name"
    dest1.price = 213.22
    dest1.image = "url"

    dest2 = Destination()
    dest2.id = 2
    dest2.desc = "Description"
    dest2.name = "name"
    dest2.price = 213.22
    dest2.image = "url"

    dest3 = Destination()
    dest3.id = 3
    dest3.desc = "Description"
    dest3.name = "name"
    dest3.price = 213.22
    dest3.image = "url"

    return JsonResponse([dest1.to_json_map(), dest2.to_json_map(), dest3.to_json_map()], safe=False)
