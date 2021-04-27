from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    # GET/POST => /api/articles/
    path('articles/', views.article_list_or_create),

    # GET/PUT/DELETE => /api/articles/1/
    path('articles/<int:article_pk>/', views.article_detail_or_update_or_delete),

]