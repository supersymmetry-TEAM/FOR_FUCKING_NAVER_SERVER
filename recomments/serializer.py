from rest_framework import serializers
from .models import  Refoodcomment
from rest_framework.response import Response

class RefoodcommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refoodcomment
        exclude = ()