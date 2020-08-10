from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserProfile, Sessions
from .serializers import UserProfileSerializer, SessionSerializer
from django.db.models import Q
from datetime import datetime
from .session_utility import utitliy
import rabbitmq.sender
import rabbitmq.receiver

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
    """
    Handles the Session Requests. It has GET, POST methods
    """
    def get(self, request):
        """
        :param request: Parameters in
        :return: Number of Sessions for the User with the given Credentials in JSON format
        """
        if request is None:
            return Response({"failed": "No credentials Provided"})

        email = request.GET['email']
        password = request.GET['password']
        mobile = request.data.GET['mobile']

        if not utitliy.Utility.check_cred_validity(password=password, email=email, mobile=mobile):
            return Response({"failed": "Invalid Username/Password"})

        user_instance = UserProfile.objects.filter(email=email, password=password)

        if user_instance is None or len(user_instance) == 0:
            return Response({"failed": "Invalid Username/Password"})

        session_instances = Sessions.objects.filter(user=user_instance[0])

        if session_instances is None or len(session_instances) == 0:
            return Response({"success": "No Active Sessions"})

        return Response({"success": len(session_instances)})

    def post(self, request):
        """
        Creates a new Session in oneToMany relationship with existing User. Accepts the Credentials in
        (Email,Password) or (Mobile,Password).
        :param request: The Parameters or Payloads sent by client
        :return: JSON Response contain

        EDIT: Now it is sending the user_id to RabbitMQ which will save dummy data
        """
        email = request.data.get('email')
        password = request.data.get('password')
        mobile = request.data.get('mobile')

        if not utitliy.Utility.check_cred_validity(password=password, email=email, mobile=mobile):
            return Response({"failed": "Invalid Username/Password"})

        if email is not None:
            user_instance = UserProfile.objects.filter(email=email, password=password)
            if user_instance is None or len(user_instance) == 0:
                return Response({"failed": "Invalid Username/Password"}, status=500)

            # Data which will be saved in the DB
            request_ = {'user_id': user_instance[0].id, 'session': str(datetime.now()),
                        'createdAt': str(datetime.now()), 'deviceDetail': "default-device"}

            serializer = SessionSerializer(data=request_)
            if serializer.is_valid(raise_exception=True):

                #####################
                sender = rabbitmq.sender.Sender()
                sender.publish(payload={"user_id": user_instance[0].id})
                return Response({'success': 'Session created'})

        elif mobile is not None:
            user_instance = UserProfile.objects.filter(mobile=mobile, password=password)
            if user_instance is None or len(user_instance) == 0:
                return Response({"failed": "Invalid Mobile/Password"}, status=500)
