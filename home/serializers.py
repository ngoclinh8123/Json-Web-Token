from rest_framework import serializers

class InforSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=255)
    age=serializers.IntegerField()