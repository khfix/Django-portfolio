from rest_framework import serializers
from .models import Me


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Me
        fields = '__all__'
        
