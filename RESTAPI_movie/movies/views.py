# rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# serialzier
from .serializers import MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewSerializer, CommentSerializer

# models
from .models import Movie, Review, Comment

# get object
from django.shortcuts import get_object_or_404

# from django.shortcuts import render

@api_view(['GET', 'POST'])
def movie_list_or_create(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovietSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
     
@api_view(['GET', 'PUT'])
def movie_detail_or_update_or_delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(instance=movie)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # data를 instance를 넣어줌(GET과의 차이점)
        serializer = MovieSerializer(instance=movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def review_list_or_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_or_update_or_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(instance=review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # data를 instance를 넣어줌(GET과의 차이점)
        serializer = ReviewSerializer(instance=review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        review.delete()
        # review_pk 로 해야 오류 안남(review.pk면 이미 삭제된 pk이므로 안됨)
        data = {
            "success": True,
            "message": f'{review_pk}가 삭제되었습니다.'
        }
        return Response(data, status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def comment_list_or_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['PUT', 'DELETE'])
# def comment_detail_or_update_or_delete(request, movie_pk, review_pk, comment_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     review = get_object_or_404(Review, pk=review_pk)
#     comment = get_object_or_404(Comment, pk=review_pk)
#     if request.method == 'PUT':
#         # data를 instance를 넣어줌(GET과의 차이점)
#         serializer = CommentSerializer(instance=review, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#     elif request.method == 'DELETE':
#         review.delete()
#         # review_pk 로 해야 오류 안남(review.pk면 이미 삭제된 pk이므로 안됨)
#         data = {
#             "success": True,
#             "message": f'{review_pk}가 삭제되었습니다.'
#         }
#         return Response(data, status.HTTP_204_NO_CONTENT)





    
