from rest_framework import serializers

from .models import Category
from checklist.serializers import Category2Serializer

class CategorySerializer(serializers.ModelSerializer):
    # created_by = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    # update_by = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Category
        fields = '__all__'


class CategoryStringSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    update_by = serializers.StringRelatedField()
    checklist_id = Category2Serializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'
 

   

