from rest_framework import serializers
from .models import CardModel,CategoryModel

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardModel
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'