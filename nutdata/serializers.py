from rest_framework import serializers
from .models import NutData_1

class NutDataSerializer_1(serializers.ModelSerializer):
    class Meta:
        model = NutData_1
        fields = '__all__'


