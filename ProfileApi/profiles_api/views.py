from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
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

    def put(self, request, pk=None):
        """
        Updates the Entire object with the provided
        :parameter
        :param request Contains the object which will replace an existing object
        :param pk Primary Key of the object that has to be updated
        """

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """
        Updates only some properties of the already existing entry/object
        :parameter
        :param request Contains the properties which will update the properties of existing object
        :param pk Primary Key of the object that has to be updated
        """

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """
        Deletes the existing object
        :parameter
        :param pk Primary Key of the object that has to be deleted
        """

        return Response({'method': 'DELETE'})


class HelloViewSet(ViewSet):
    """Test View Set"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello Message"""
        an_api = [
            'Users HTTP Method as function (get, post, patch, put, delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message': 'Hello!', 'a_viewset': an_api})

    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})

