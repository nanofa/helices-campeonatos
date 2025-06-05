from rest_framework import serializers
from .models import Tiro

class TiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiro
        fields = '__all__'
