
from rest_framework import serializers
from .models import Foodcomment
from rest_framework.response import Response
from recomments.models import Refoodcomment 
class FoodCommentSerializer(serializers.ModelSerializer):
    reconum = serializers.SerializerMethodField()
    class Meta:
        model = Foodcomment
        exclude = ()
    def get_reconum(self, obj):
        reconum = Refoodcomment.objects.filter(foodcomment__in=[obj]).count()
        return reconum
    
class WriteFoodCommentSerializer(serializers.ModelSerializer):

    
    def create(self, validated_data):
        return Foodcomment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.food = validated_data.get("food", instance.food)
        instance.token = validated_data.get("token", instance.token)
        instance.author = validated_data.get("author", instance.author)
        instance.text = validated_data.get("text", instance.text)

        instance.save()
        print(validated_data)
        return instance

    class Meta:
        model = Foodcomment
        exclude = ()
class DelFoodCommentSerializer(serializers.ModelSerializer):

    
    def create(self, validated_data):
        return Foodcomment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.food)
        instance.token = validated_data.get("token", instance.token)
        if instance.token == Foodcomment.objects.get(pk=instance.id):
            instance.delete()
            return []
        return instance

    class Meta:
        model = Foodcomment
        exclude = ("created_date",)
    