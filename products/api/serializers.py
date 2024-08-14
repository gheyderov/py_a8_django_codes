from rest_framework import serializers
from products.models import Category, Tag, Recipe


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'id',
            'title'
        ]


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = [
            'id',
            'title'
        ]


class RecipeSerializer(serializers.ModelSerializer):

    # category = serializers.CharField(source = 'category.title')
    category = CategorySerializer()
    tags = TagSerializer(many = True)

    class Meta:
        model = Recipe
        fields = [
            'id',
            'title',
            'cover_image',
            'small_description',
            'description',
            'author_name',
            'category',
            'tags'
        ]



class RecipeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = [
            'id',
            'title',
            'cover_image',
            'small_description',
            'description',
            'author',
            'category',
            'tags'
        ]