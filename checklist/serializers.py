from rest_framework import serializers

from .models import Checklist, ChecklistTranslation

from category.serializers import CategoryStringSerializer
from category.models import Category
from drf_nested_serializer import NestedModelSerializer

class Category2Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Checklist
        fields = ('id','steps', 'category', 'created_by', 'update_by')


class Category2ChecklistSerializer(serializers.ModelSerializer):
    
    created_by = serializers.StringRelatedField()
    update_by = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    class Meta:
        model = Checklist
        fields = "__all__"
    



class ChecklistTranslationPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChecklistTranslation
        fields = ('id', 'language', 'description', 'checklist')


class ChecklistTranslationStringSerializer(serializers.ModelSerializer):
    checklist = Category2ChecklistSerializer(many=False, read_only = True)
    language = serializers.StringRelatedField()
    class Meta:
        model = ChecklistTranslation
        fields = ('id', 'language', 'description', 'checklist')
    

class CategoryChecklistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class ChecklistDetailSerializers(NestedModelSerializer):
    
    class Meta:
        model = Checklist
        fields = "__all__"
        nested_fields = {'checklist_translation_id': 'checklist', 'category': 'category'}