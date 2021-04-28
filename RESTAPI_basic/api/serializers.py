# serializers,py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(min_length=2, max_length=100)
    class Meta:
        model = Article
        fields = '__all__'

class ArticleListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(min_length=2, max_length=100)
    content = serializers.CharField(min_length=2)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = Article
        fields = '__all__'