from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField(auto_now=True) # updated를 기준으로 맞춤
    poster_path = models.CharField(max_length=200)


class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")


class Comment(models.Model):
    content = models.CharField(max_length=100)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comments")