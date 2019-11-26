from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Movie, Genre, Actor, Review, Article, RootReview

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'name_en', 'birthday', 'profile_path']

class GenreSerializer(serializers.ModelSerializer):
    like_users = UserSerializer(many=True)
    class Meta:
        model = Genre
        fields = ['id', 'name', 'like_users']

class RootSerializer(serializers.ModelSerializer):
    movie_id = serializers.IntegerField(source='review.movie.id')
    class Meta:
        model = RootReview
        fields = ['id', 'content', 'score', 'user', 'movie_id', 'created_at']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'content', 'score', 'user', 'movie', 'created_at']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'content', 'score', 'user', 'created_at']

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genres = GenreSerializer(many=True)
    like_users = UserSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id', 'title', 'original_title', 'poster_url', 'actors', 'description', 'score', 'open_date', 'genres', 'like_users', 'director', 'video', 'country']

class Actor2Serializer(serializers.ModelSerializer):
    like_users = UserSerializer(many=True)
    filmography = MovieSerializer(many=True)
    class Meta:
        model = Actor
        fields = ['id', 'name', 'name_en', 'birthday', 'profile_path', 'like_users', 'filmography']

class User2Serializer(serializers.ModelSerializer):
    like_movies = MovieSerializer(many=True)
    like_genres = GenreSerializer(many=True)
    like_actors = ActorSerializer(many=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'like_movies', 'like_genres', 'like_actors')