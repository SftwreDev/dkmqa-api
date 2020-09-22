from rest_framework import serializers

from .models import Recipient_Email


class RecipientEmailFormSerializers(serializers.ModelSerializer):
    class Meta:
        model = Recipient_Email
        fields = '__all__'


class RecipientEmailStringSerializers(serializers.ModelSerializer):
    plant = serializers.StringRelatedField()
    shift = serializers.StringRelatedField()
    person = serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()
    updated_by = serializers.StringRelatedField()

    class Meta:
        model = Recipient_Email
        fields = '__all__'