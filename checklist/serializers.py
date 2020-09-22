from rest_framework import serializers

from .models import Checklist



class Category2Serializer(serializers.ModelSerializer):
    

    class Meta:
        model = Checklist
        fields = ('id','steps', 'category', 'description', 'created_by', 'update_by')


class Category2ChecklistSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()
    update_by = serializers.StringRelatedField()
    class Meta:
        model = Checklist
        fields = ('id','steps', 'category', 'description', 'created_by', 'update_by')
    