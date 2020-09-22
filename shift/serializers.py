from rest_framework import serializers

from .models import Shift , ShiftCode


class ShiftCodeFormSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShiftCode
        fields = '__all__'


class ShiftCodeStringSerializers(serializers.ModelSerializer):
    client = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()
    updated_by = serializers.StringRelatedField()
    
    class Meta:
        model = ShiftCode
        fields = '__all__'


class ShiftFormSerializers(serializers.ModelSerializer):
    shift_hour = serializers.TimeField(format='%H:%M')
    start_time = serializers.TimeField(format='%H:%M')
    end_time = serializers.TimeField(format='%H:%M')
    class Meta:
        model = Shift
        fields = '__all__'


class ShiftStringSerializers(serializers.ModelSerializer):
    client = serializers.StringRelatedField()
    shift_code = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()
    updated_by = serializers.StringRelatedField()
    class Meta:
        model = Shift
        fields = '__all__'