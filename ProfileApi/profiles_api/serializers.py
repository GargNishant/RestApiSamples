from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our ApiView"""
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    # We are validating the  field for various fields
    name = serializers.CharField(max_length=10)
    age = serializers.IntegerField(min_value=19, max_value=200)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serialize the User Profile API. It uses the UserProfileModel"""

    # Connect the serializer with a specific model in our project
    # When creating a new object, Meta will validate the fields against the model
    # After success, the create method will be create
    class Meta:
        model = models.UserProfile

        # The Fields that the serializer can work with across all api. Thus the Serializer will pass
        # id, email, name, and password when get, post, put, patch, delete is called
        fields = ('id', 'email', 'name', 'password')

        # configuring the password field as we don't want to give the has of password to user
        extra_kwargs = {
            'password': {
                # This makes the password field as write only, Meaning it can only be created or updated
                # But the password will never be given back to the user in get or other requests
                'write_only': True,
                # Changing the Password field input type. This only affects the browsable api (Browser version)
                'style': {'input_type': 'password'}
            }
        }

    # Overriding the create function. Mainly to store password as HASH instead of plain text
    def create(self, validated_data):
        """ Create and return new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """Handles updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)




