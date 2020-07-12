from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our ApiView"""
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    # We are validating the  field for various fields
    name = serializers.CharField(max_length=10)
    age = serializers.IntegerField(min_value=19, max_value=200)
