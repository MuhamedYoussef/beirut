from rest_framework import serializers
from .models import AidRecord


class AidRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AidRecord
        fields = '__all__'