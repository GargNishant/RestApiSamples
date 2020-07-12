from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

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
        return Response({'message': 'Hello!', 'an_apiview': an_api}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """Create a hello message with our name"""

        # The data is passed as request.data. We then
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

