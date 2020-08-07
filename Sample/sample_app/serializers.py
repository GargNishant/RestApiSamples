from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.Serializer):
    # Upon Omitting a field, the field will not be passed as json
    firstName = serializers.CharField(max_length=30)
    lastName = serializers.CharField(max_length=100)
    address = serializers.CharField()
    mobile = serializers.IntegerField()
    email = serializers.EmailField()
    isActive = serializers.BooleanField(default=True)
    # DOCS: https://www.django-rest-framework.org/api-guide/fields/
    # Write only makes the field to be only created or modified, not avail for reading or GET
    password = serializers.CharField(min_length=10, max_length=200, write_only=True)
    # Read only make it only for Read or GET. Ignored when trying to modify or create it by args or POST,PUT etc
    id = serializers.IntegerField(read_only=True)

    def update(self, instance, validated_data):
        # Work in Progress
        """
        Updates the already present of the instance of User profile
        :param instance: Instance of the existing User Profile. This instance will be updated and saved again
        :param validated_data: The data after it has been validated and transformed by some ways before storing
        """
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.lastName = validated_data.get('lastName', instance.lastName)
        instance.address = validated_data.get('address', instance.address)
        instance.email = validated_data.get('email', instance.email)
        instance.mobile = validated_data.get('mobile', instance.mobile)

        instance.save()
        return instance

    def create(self, validated_data):
        return UserProfile.objects.create(**validated_data)