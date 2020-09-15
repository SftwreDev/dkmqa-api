from rest_framework import serializers

from .models import Category1, Category2, Category3


class Category1Serializer(serializers.ModelSerializer):

    class Meta:
        model = Category1
        fields = '__all__'

 
class Category2Serializer(serializers.ModelSerializer):
    # categoryName = serializers.StringRelatedField(many=True)
    # categoryName = serializers.SlugRelatedField(read_only=True, slug_field='name')
    # checklist = Category1Serializer(many=False, read_only=True)
    class Meta:
        model = Category2
        fields = ('id','steps', 'categoryID', 'description', 'created_by')


class Category2ChecklistSerializer(serializers.ModelSerializer):
    categoryID = serializers.StringRelatedField()
    # categoryName = serializers.SlugRelatedField(read_only=True, slug_field='name')
    # checklist = Category1Serializer(many=False, read_only=True)
    class Meta:
        model = Category2
        fields = ('id','steps', 'categoryID', 'description', 'created_by')
    

class Category3Serializer(serializers.ModelSerializer):
    # categoryName = serializers.StringRelatedField()
    
    class Meta:
        model = Category3
        fields = ('id','steps', 'categoryID', 'description', 'created_by')       



class Category3DefectCodesSerializer(serializers.ModelSerializer):
    categoryID = serializers.StringRelatedField()
    
    class Meta:
        model = Category3
        fields = ('id','steps', 'categoryID', 'description', 'created_by')     

   

