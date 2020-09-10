from rest_framework import serializers

from .models import Category1, Category2, Category3


class Category1Serializer(serializers.ModelSerializer):

    class Meta:
        model = Category1
        fields = '__all__'


 
class Category2Serializer(serializers.ModelSerializer):
    categoryName = serializers.StringRelatedField()
    class Meta:
        model = Category2
        fields = ('id','steps', 'description','created_by' , 'categoryName')



class Category3Serializer(serializers.ModelSerializer):
<<<<<<< HEAD
    categoryName = serializers.StringRelatedField()
    class Meta:
        model = Category3
        fields = ('id','steps', 'description','created_by' , 'categoryName')             
=======
    category1ID = serializers.StringRelatedField()
    class Meta:
        model = Category3
        fields = ('steps', 'description','created_by' , 'category1ID')             
>>>>>>> 75640c6d1d727d7249a837047c43e709ee45ae0a
