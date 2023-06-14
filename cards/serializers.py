from rest_framework import serializers
from .models import CardModel,CategoryModel,CardImage

class CardImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardImage
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    images = CardImageSerializer(many=True, read_only=True)
    class Meta:
        model = CardModel
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'