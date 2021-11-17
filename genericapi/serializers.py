from rest_framework import serializers
from .models import TestModel

class TestSerializers(serializers.Serializer):
    id          = serializers.IntegerField(read_only= True)
    name        = serializers.CharField()
    description = serializers.CharField()
    phone       = serializers.IntegerField()
    is_alve     = serializers.BooleanField()
    extra_name  = serializers.CharField(read_only= True)
    amount      = serializers.FloatField()
    created_at  = serializers.DateTimeField(read_only= True)
    updated_at  = serializers.DateTimeField(read_only= True)


    def create(self, validated_data):
        return  TestModel.objects.create(**validated_data)


