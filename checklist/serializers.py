from rest_framework import serializers

from .models import Checklist, ChecklistTranslation

from category.serializers import CategoryStringSerializer
from category.models import Category, CategoryTranslation
from drf_nested_serializer import NestedModelSerializer

class ChecklistCategory(serializers.ModelSerializer):
    class Meta:
        model = CategoryTranslation
        fields = ('id', 'name')


class Checklist_Translation(serializers.ModelSerializer):
    class Meta:
        model = ChecklistTranslation
        fields = ('language_id', 'description')




class Category2ChecklistSerializer(serializers.ModelSerializer):
    
    created_by = serializers.StringRelatedField()
    update_by = serializers.StringRelatedField()
    checklist_translation = Checklist_Translation(many=True, read_only=True)
    category = ChecklistCategory(many=False, read_only=True)
    class Meta:
        model = Checklist
        fields = ('id', 'steps','category',  'checklist_translation','created_by',  'date_created','update_by','date_updated' )
    



class ChecklistTranslationPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChecklistTranslation
        fields = ('id', 'language', 'description', 'checklist')


class ChecklistTranslationStringSerializer(serializers.ModelSerializer):
    
    language = serializers.StringRelatedField()
    class Meta:
        model = ChecklistTranslation
        fields = ('id', 'language', 'description', 'checklist_id')
    

class CategoryChecklistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class ChecklistTranslationSerialize(serializers.ModelSerializer):
    class Meta:
        model = ChecklistTranslation
        fields = ('id', 'language', 'description')


class Category2Serializer(serializers.ModelSerializer):
    checklist_translation = ChecklistTranslationSerialize(many=True)
    # category = ChecklistCategory(many=True)
    class Meta:
        model = Checklist
        fields = ('id','steps', 'category', 'checklist_translation', 'created_by', 'date_created', 'update_by', 'date_updated')

    def create(self, validated_data):
        translations = validated_data.pop('checklist_translation')
        checklist = Checklist.objects.create(**validated_data)
        for translation in translations:
            ChecklistTranslation.objects.create(checklist=checklist, **translation)
        return checklist
    
    def update(self, instance, validated_data):
        translations = validated_data.pop('checklist_translation')
        checklist = (instance.checklist_translation).all()
        checklist = list(checklist)
        # instance.language = validated_data.get('language', instance.language)
        # instance.name = validated_data.get('name', instance.name)
        instance.steps = validated_data.get('steps', instance.steps)
        instance.category = validated_data.get('category', instance.category)
        instance.save()

        for translation in translations:
            checklist = checklist.pop(0)
            checklist.description = translation.get('description', checklist.description)
            checklist.language = translation.get('language', checklist.language)
            checklist.save()
        return instance