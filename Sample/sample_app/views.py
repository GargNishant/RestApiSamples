from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserProfile, Sessions
from .serializers import UserProfileSerializer, SessionSerializer
from django.db.models import Q
from datetime import datetime
from .session_utility import utitliy
import rabbitmq.sender

# Create your views here.


class UserProfileView(APIView):

    @staticmethod
    def get(request, username=None, mobile=None):

        if username is not None or mobile is not None:
            try:
                user_profiles = UserProfile.objects.get(Q(email=username) | Q(mobile=mobile))
                serializer = UserProfileSerializer(user_profiles)
                return Response({'userProfiles': serializer.data})
            except ObjectDoesNotExist:
                return Response({"failed": "UserName/Mobile not Registered"}, status=404)

        else:
            user_profiles = UserProfile.objects.all()
            serializer = UserProfileSerializer(user_profiles, many=True)
            return Response({'userProfiles': serializer.data})

    @staticmethod
    def post(request):
        user_profile = request.data.get('user-profile')

        if user_profile is None:
            return Response({"failed": "user-profile not found"}, status=500)

        password = request.GET.get('password', None)
        email = request.GET.get('email', None)
        mobile = request.GET.get('mobile', None)

        if not utitliy.Utility.check_cred_validity(password=password, email=email, mobile=mobile):
            return Response({"failed": "Invalid Username/Password"})

        user_instance = UserProfile.objects.filter(Q(email=user_profile['email']) | Q(mobile=user_profile['mobile']))

        if len(user_instance) > 0:
            return Response({"failed": "Username or Mobile already taken"}, status=500)

        serializer = UserProfileSerializer(data=user_profile)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
            return Response({"success": "User '{}' created Successfully".format(user_saved.firstName)})

    @staticmethod
    def put(request, pk):
        if pk is None or type(pk) != int:
            return Response({"failed": "Invalid Id"}, status=500)

        user_profile = get_object_or_404(UserProfile.objects.all(), pk=pk)
        data = request.data.get('user-profile')
        if data is None:
            return Response({"failed": "user-profile not found"}, status=500)

        serializer = UserProfileSerializer(instance=user_profile, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
            return Response({"Success": "User {} Updated Successfully".format(user_saved.firstName)})


class SessionView(APIView):
    """
    Handles the Session Requests. It has GET, POST methods
    """

    @staticmethod
    def get(request):
        """
        Query's the Database to find if there are and how many active sessions are present against
        given user credentials
        :param request: Expected are password and Mobile/Username
        :return: Number of Sessions for the User
        """
        if request is None:
            return Response({"failed": "No credentials Provided"}, status=500)

        if request.GET.get('password') is None:
            return Response({'failed': 'No password Provided'}, status=404)

        password = request.GET.get('password', None)
        email = request.GET.get('email', None)
        mobile = request.GET.get('mobile', None)

        if not utitliy.Utility.check_cred_validity(password=password, email=email, mobile=mobile):
            return Response({"failed": "Invalid Username/Password"})

        # Checking number of sessions
        try:
            user_instance = UserProfile.objects.get((Q(email=email) | Q(mobile=mobile)), password=password)
            session_instances = Sessions.objects.filter(user=user_instance)

            if len(session_instances) == 0:
                return Response({"success": "No Active Sessions"})
            return Response({"success": len(session_instances)})

        except ObjectDoesNotExist:
            return Response({"failed": "Invalid Username/Password"})

    @staticmethod
    def post(request):
        """
        Creates a new Session in oneToMany relationship with existing User. Accepts the Credentials in
        (Email,Password) or (Mobile,Password).
        :param request: The Parameters or Payloads sent by client
        :return: JSON Response containing result

        EDIT: Now it is sending the user_id to RabbitMQ which will save dummy data
        """
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        mobile = request.data.get('mobile', None)

        if not utitliy.Utility.check_cred_validity(password=password, email=email, mobile=mobile):
            return Response({"failed": "Invalid Username/Password"})

        try:
            user_profile = UserProfile.objects.get(Q(password=password), (Q(email=email) | Q(mobile=mobile)))
            data = {'user_id': user_profile.id, 'session': str(datetime.now()),
                    'createdAt': str(datetime.now()), 'deviceDetail': "default-device"}

            serializer = SessionSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                sender = rabbitmq.sender.Sender()
                sender.publish(payload={"session": data})
                return Response({'success': 'Session created'})

        except ObjectDoesNotExist:
            return Response({"failed": "Username/Password not registered"})

