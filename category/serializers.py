from rest_framework import serializers

from .models import Category , CategoryTranslation
from drf_nested_serializer import NestedModelSerializer

###################### Category Translations Serializers ########################

class CategoryTranslationSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryTranslation
        fields = '__all__'


class CategoryTranslationStringSerializers(serializers.ModelSerializer):
    language = serializers.StringRelatedField()
    class Meta:
        model = CategoryTranslation
        fields = '__all__'

###################### Category Serializers ########################

class CategorySerializer(serializers.ModelSerializer):
    # created_by = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    # update_by = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Category
        fields = '__all__'


class CategoryStringSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    update_by = serializers.StringRelatedField()
    category = CategoryTranslationStringSerializers(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'
 



