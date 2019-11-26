from django.shortcuts import render, get_object_or_404
from .models import Movie, Review, RootReview, Article, Genre
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import MovieSerializer, ReviewSerializer, ArticleSerializer, RootSerializer, UserSerializer, GenreSerializer
from django.contrib.auth import get_user_model

from IPython import embed

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def index(request):
    movies = Movie.objects.all()
    serializers = MovieSerializer(movies, many=True)
    return Response(serializers.data)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def genre_index(request):
    genres = Genre.objects.all()
    serializers = GenreSerializer(genres, many=True)
    return Response(serializers.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializers = MovieSerializer(movie)
    return Response(serializers.data)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = get_user_model().objects.get(pk=request.data.get('user_id'))
    # embed()
    if request.method == 'POST':
        is_liked = True
        if user in movie.like_users.all():
            movie.like_users.remove(user)
            print('삭제')
            is_liked = False
        else:
            movie.like_users.add(user)
            print('추가')
            is_liked = True
    else:
        if user in movie.like_user.all():
            is_liked = True
        else:
            is_liked = False
    like_count = movie.like_users.count()
    return Response({'is_liked': is_liked, 'like_count': like_count})
    

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def review(request):
    if request.method == 'GET':
        reviews = RootReview.objects.all()
        serializers = RootSerializer(reviews, many=True)
    else:
        serializers = ReviewSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data)
    return Response(serializers.data)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def article(request):
    serializers = ArticleSerializer(data=request.data)
    if serializers.is_valid(raise_exception=True):
        serializers.save()
        return Response(serializers.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def update_delete(request, review_pk):
    review = get_object_or_404(RootReview, pk=review_pk)
    if request.method == 'PUT':
        serializer = ReviewSerializer(data=request.data, instance=review)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        review.delete()
        return Response({'status': 204, 'message': '삭제되었습니다.'})

@api_view(['PUT'])
@permission_classes([IsAuthenticatedOrReadOnly])
def update(request, review_pk):
    review = get_object_or_404(RootReview, pk=review_pk)
    serializer = ArticleSerializer(data=request.data, instance=review)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def user_detail(request, user_pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=user_pk)
    serializers = UserSerializer(user)
    return Response(serializers.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def user_index(request):
    User = get_user_model()
    users = User.objects.all()
    serializers = UserSerializer(users, many=True)
    return Response(serializers.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def user_update_delete(request, user_pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=user_pk)
    if request.method == 'PUT':
        user.like_genres.remove()
        for like_genre in request.data.get("like_genres"):
            genre = get_object_or_404(Genre, pk=like_genre["id"])
            user.like_genres.add(genre)
        user.like_actors.remove()
        for like_actor in request.data.get("like_actors"):
            actor = get_object_or_404(Actor, pk=like_actor["id"])
            user.like_actors.add(actor)
        user.like_movies.remove()
        for like_movies in request.data.get("like_movies"):
            movie = get_object_or_404(Movie, pk=like_movie["id"])
            user.like_movies.add(genre)
        user.save()
        return Response({'status': 204, 'message': '등록되었습니다.'})
    else:
        user.delete()
        return Response({'status': 204, 'message': '삭제되었습니다.'})