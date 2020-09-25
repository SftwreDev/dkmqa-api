from rest_framework import serializers

from .models import Checklist, ChecklistTranslation



class ChecklistTranslationPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChecklistTranslation
        fields = ('id', 'language', 'description')


class ChecklistTranslationStringSerializer(serializers.ModelSerializer):
    language = serializers.StringRelatedField()
    class Meta:
        model = ChecklistTranslation
        fields = ('id', 'language', 'description')
    

class Category2Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Checklist
        fields = ('id','steps', 'category', 'description', 'created_by', 'update_by', 'translation')


class Category2ChecklistSerializer(serializers.ModelSerializer):
    
    category = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()
    update_by = serializers.StringRelatedField()
    translation = ChecklistTranslationStringSerializer(many=False, read_only=True)
    class Meta:
        model = Checklist
        fields = ('id','steps', 'category', 'description', 'created_by', 'update_by', 'translation')
    

