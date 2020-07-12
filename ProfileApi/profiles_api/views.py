from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    # noinspection PyMethodMayBeStatic
    def get(self, request, format=None):
        """
        Returns a list of API View Features
        :parameter
        :param request Contains the parameters send
        :param format Format of the response. NOT IN USE
        """
        an_api = [
            'Users HTTP Method as function (get, post, patch, put, delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_api})
