from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    # def update(self, instance, validate_data):
    #     instance.title= validate_data.get('title', instance.title)
    #     instance.description= validate_data.get('description', instance.description)
    #     instance.text= validate_data.get('text', instance.text)
    #     instance.author= validate_data.get('author', instance.author)
    #     instance.created_date= validate_data.get('created_date', instance.created_date)
    #     instance.published_date= validate_data.get('published_date', instance.published_date)
    #     instance.thumbnail_image= validate_data.get('thumbnail_image', instance.thumbnail_image)
    #     instance.feature_image= validate_data.get('feature_image', instance.feature_image)
    #     instance.category= validate_data.get('category', instance.category)
    #     instance.tag= validate_data.get('tag', instance.tag)

    #     instance.save()
    #     return instance

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
