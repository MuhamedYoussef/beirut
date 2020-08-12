from rest_framework import serializers
from .models import AidRecord, Offer


class AidRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AidRecord
        fields = '__all__'



class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'