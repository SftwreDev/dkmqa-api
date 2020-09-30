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

class CategoryTranslationSerialize(serializers.ModelSerializer):
    
    class Meta:
        model = CategoryTranslation
        fields = ('language', 'name')
        
###################### Category Serializers ########################

# class CategorySerializer(serializers.ModelSerializer):
#     # created_by = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
#     # update_by = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    
#     class Meta:
#         model = Category
#         fields = ('id', 'steps', 'date_created', 'created_by', 'date_updated', 'update_by')


class CategoryStringSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    update_by = serializers.StringRelatedField()
    category_translation = CategoryTranslationSerialize(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'steps', 'category_translation', 'date_created', 'created_by', 'date_updated', 'update_by')
 

class CategorySerializer(serializers.ModelSerializer):
    # created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # update_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    category_translation = CategoryTranslationSerialize(many=True)
    class Meta:
        model = Category
        fields = ('id','steps', 'category_translation', 'date_created', 'created_by', 'date_updated', 'update_by')

    def create(self, validated_data):
        translations = validated_data.pop('category_translation')
        category = Category.objects.create(**validated_data)
        for translation in translations:
            CategoryTranslation.objects.create(category=category, **translation)
        return category
    
    def update(self, instance, validated_data):
        translations = validated_data.pop('category_translation')
        category = (instance.category_translation).all()
        category = list(category)
        # instance.language = validated_data.get('language', instance.language)
        # instance.name = validated_data.get('name', instance.name)
        instance.steps = validated_data.get('steps', instance.steps)
        instance.save()

        for translation in translations:
            category = category.pop(0)
            category.name = translation.get('name', category.name)
            category.language = translation.get('language', category.language)
            category.save()
        return instance