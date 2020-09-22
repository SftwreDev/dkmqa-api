from rest_framework import serializers

from .models import Language


class LanguageFormSerializers(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class LanguageStringSerializers(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    updated_by = serializers.StringRelatedField()
    
    class Meta:
        model = Language
        fields = '__all__'