from rest_framework import serializers

from .models import  Defectcodes, DefectcodesTranslation
from drf_nested_serializer import NestedModelSerializer

class DefectCodesTranslationSerializers(serializers.ModelSerializer):
    class Meta:
        model = DefectcodesTranslation
        fields = '__all__'

class DefectCodesTranslationStringSerializers(serializers.ModelSerializer):
    # defect_code = serializers.StringRelatedField()
    language = serializers.StringRelatedField()
    class Meta:
        model = DefectcodesTranslation
        fields = ('id','defect_code_id' , 'language', 'description')

class DefectCodesTranslate(serializers.ModelSerializer):
    class Meta:
        model = DefectcodesTranslation
        fields = ('language_id', 'description')

class DefectCodesTranslateCreate(serializers.ModelSerializer):
    class Meta:
        model = DefectcodesTranslation
        fields = ['language', 'description']
        

class Category3Serializer(serializers.ModelSerializer):
    defect_code_translation = DefectCodesTranslateCreate(many=True)
        
    class Meta:
        model = Defectcodes
        fields = ('id','steps', 'defect_code_translation',  'created_by', 'date_created' , 'update_by', 'date_updated')
        
    def create(self, validated_data):
        translations = validated_data.pop('defect_code_translation')
        defect_code = Defectcodes.objects.create(**validated_data)
        for translation in translations:
            DefectcodesTranslation.objects.create(defect_code=defect_code, **translation)
        return defect_code
    
    def update(self, instance, validated_data):
        translations = validated_data.pop('defect_code_translation')
        defect_codes = (instance.defect_code_translation).all()
        defect_codes = list(defect_codes)
        # instance.language = validated_data.get('language', instance.language)
        # instance.name = validated_data.get('name', instance.name)
        instance.steps = validated_data.get('steps', instance.steps)
        instance.save()

        for translation in translations:
            defect_codes = defect_codes.pop(0)
            defect_codes.description = translation.get('description', defect_codes.description)
            defect_codes.language = translation.get('language', defect_codes.language)
            defect_codes.save()
        return instance


class Category3DefectCodesSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    update_by = serializers.StringRelatedField()
    defect_code_translation = DefectCodesTranslate(many=True, read_only=True)

    class Meta:
        model = Defectcodes
        fields = ('id','steps', 'defect_code_translation', 'created_by', 'date_created', 'update_by', 'date_updated')     

    



