from rest_framework import serializers
from .models import Clothes, Category, Brand, ClothesInStock, ClothesColor, ClothesSize
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id username email'.split()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id category_name category_slug category_description'.split()


class CategoryDetailSerializer(serializers.ModelSerializer):
    # category_slug = serializers.SlugRelatedField(slug_field='clothes_name', read_only=True, many=True)
    clothes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = 'id category_name category_slug category_description clothes'.split()


class ClothesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = 'id clothes_name clothes_slug clothes_price clothes_image clothes_brand'.split()


class ClothesColorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothesColor
        fields = 'id color_name color_slug'.split()


class ClothesSizeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothesSize
        fields = 'id ch eu us'.split()


class ClothesInStockListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothesInStock
        fields = 'id clothes clothes_color clothes_size clothes_count'.split()


