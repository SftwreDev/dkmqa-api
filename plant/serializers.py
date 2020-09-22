from rest_framework import serializers

from .models import Address, Plant


class AdddressFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class AdddressStringSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    updated_by = serializers.StringRelatedField()
    class Meta:
        model = Address
        fields = "__all__"

class PlantFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = "__all__"

class PlantStringSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    updated_by = serializers.StringRelatedField()
    class Meta:
        model = Plant
        fields = "__all__"