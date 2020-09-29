from rest_framework import serializers

from .models import  Defectcodes
from drf_nested_serializer import NestedModelSerializer

class Category3Serializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Defectcodes
        fields = ('id','steps', 'category', 'description', 'created_by', 'update_by')       



class Category3DefectCodesSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()
    update_by = serializers.StringRelatedField()
    class Meta:
        model = Defectcodes
        fields = ('id','steps', 'category', 'description', 'created_by', 'update_by')     

   
class DefectCodesDetailSerializer(NestedModelSerializer):
    class Meta:
        model = Defectcodes
        fields = "__all__"
        nested_fields = {'defect_codes_id': 'defect_codes'}


