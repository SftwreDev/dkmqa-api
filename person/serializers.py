from rest_framework import serializers

from .models import Person


class PersonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"



class PersonStringSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    updated_by = serializers.StringRelatedField()
    
    class Meta:
        model = Person
        fields = '__all__'


