from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('genres/', views.genre_index, name='genre_index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('reviews/', views.review, name='review'),
    path('articles/', views.article, name='article'),
    path('reviews/<int:review_pk>/', views.update_delete, name='update_delete'),
    path('articles/<int:review_pk>/', views.update, name='update'),
    path('users/<int:user_pk>/', views.user_detail),
    path('users/', views.user_index, name='user_index'),
    path('users/<int:user_pk>/update_delete/', views.user_update_delete, name='user_update_delete'),
]