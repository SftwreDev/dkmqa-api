from rest_framework import serializers

from .models import Client


class ClientFormSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ClientStringSerializers(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    updated_by = serializers.StringRelatedField()
    class Meta:
        model = Client
        fields = '__all__'