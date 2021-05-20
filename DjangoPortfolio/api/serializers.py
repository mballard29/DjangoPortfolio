from rest_framework import serializers
from .models import Project, Image, Tag, DetailBody

class ProjectSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(required=False)
    class Meta:
        model = Project
        fields = ['title', 'description', 'posted', 'tags', 'thumbnail']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image', 'project']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'type']

class DetailBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailBody
        fields = ['intro', 'body', 'project']