from rest_framework import serializers
from .models import Movie, Review, Comment

# reviewlist : 단일영화 -> 전체를 보여주는게 있어야되는데 reviewlist
# 그외에 review 수정하거나 review class 


# 단일 댓글
class CommentSerializer(serializers.ModelSerializer):
    content = serializers.CharField(max_length=100)
    class Meta:
        model = Comment
        fields = ['content']
        read_only_fields = ['review',]

# 단일 리뷰
class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=100)
    rank = serializers.IntegerField(min_value=0, max_value=100)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        # 읽기만 하는거니까 우린 신경 x
        read_only_fields = ['movie',]

# 전체 리뷰 
class ReviewListSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    class Meta:
        model = Review
        fields = ['title', 'rank', 'comment_count']

# 단일 영화 - Detail & Update & Delete
class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    poster_path = serializers.CharField(max_length=200)    
    reviews = ReviewListSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'


# 전체 영화 - List & Create
class MovieListSerializer(serializers.ModelSerializer):
    review_count = serializers.IntegerField(source='reviews.count', read_only=True)
    class Meta:
        model = Movie
        fields = ['id', 'title', 'poster_path', 'review_count',]





