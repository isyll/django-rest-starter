from rest_framework import serializers


class StandardResponseSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    status = serializers.IntegerField()
    message = serializers.CharField()
    data = serializers.JSONField()
