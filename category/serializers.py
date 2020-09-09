from rest_framework import serializers

from .models import Category1, Category2, Category3


class Category1Serializer(serializers.ModelSerializer):

    class Meta:
        model = Category1
        fields = '__all__'


 
class Category2Serializer(serializers.ModelSerializer):
    category1ID = serializers.StringRelatedField()
    class Meta:
        model = Category2
        fields = ('steps', 'description','created_by' , 'category1ID')



class Category3Serializer(serializers.ModelSerializer):
    category1ID = serializers.StringRelatedField()
    class Meta:
        model = Category3
        fields = ('steps', 'description','created_by' , 'category1ID')             