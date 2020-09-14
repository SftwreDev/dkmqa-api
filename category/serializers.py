from rest_framework import serializers

from .models import Category1, Category2, Category3


class Category1Serializer(serializers.ModelSerializer):

    class Meta:
        model = Category1
        fields = '__all__'


 
class Category2Serializer(serializers.ModelSerializer):
    # categoryName = serializers.StringRelatedField()
    # categoryName = serializers.SlugRelatedField(queryset=Category1.objects.all(), slug_field='name')
    class Meta:
        model = Category2
        fields = '__all__'

    



class Category3Serializer(serializers.ModelSerializer):
    # categoryName = serializers.StringRelatedField()
    
    class Meta:
        model = Category3
        fields = '__all__'          

    # def to_representation(self, instance):
    #     rep = super(Category3Serializer, self).to_representation(instance)
    #     rep['defect_codes'] = instance.defect_codes.name
    #     return rep

