from rest_framework import serializers
from .models import Efis,Ecam,Pfd

class EfisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Efis
        fields = '__all__'

class EcamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ecam
        fields = '__all__'

class PfdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pfd
        fields = '__all__'