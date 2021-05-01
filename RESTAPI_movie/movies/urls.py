from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('', views.movie_list_or_create),
    path('<int:movie_pk>/', views.movie_detail_or_update_or_delete),
    path('<int:movie_pk>/reviews/', views.review_list_or_create),
    path('reviews/<int:review_pk>/', views.review_detail_or_update_or_delete),
    path('reviews/<int:review_pk>/comments/', views.comment_list_or_create),
]