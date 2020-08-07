from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserProfile, Sessions
from .serializers import UserProfileSerializer
from django.db.models import Q
# Create your views here.


class UserProfileView(APIView):

    def get(self, request):
        user_profiles = UserProfile.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = UserProfileSerializer(user_profiles, many=True)
        return Response({'userProfiles': serializer.data})

    def post(self, request):
        user_profile = request.data.get('user-profile')

        # filter returns a List, while get returns single object and throws error if multiple or none
        instance = UserProfile.objects.filter(Q(email=user_profile['email']) | Q(mobile=user_profile['mobile']))
        if instance is None or len(instance) == 0:
            serializer = UserProfileSerializer(data=user_profile)
            if serializer.is_valid(raise_exception=True):
                user_saved = serializer.save()
                return Response({"success": "User '{}' created Successfully".format(user_saved.firstName)})
            return Response({"failed": "Error Validating Fields"}, status=500)
        return Response({"failed": "Username or Mobile already taken"}, status=500)

    def put(self, request, pk):
        instance = get_object_or_404(UserProfile.objects.all(), pk=pk)
        data = request.data.get('user-profile')
        serializer = UserProfileSerializer(instance=instance, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
            return Response({"Success": "User {} Updated Successfully".format(user_saved.firstName)})
        return Response({"failed": "Error"}, status=500)


class SessionView(APIView):

    def get(self, request):
        if request is None:
            return Response({"failed": "No Username or Mobile Provided"})

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
