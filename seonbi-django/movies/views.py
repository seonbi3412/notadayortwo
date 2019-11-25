from django.shortcuts import render, get_object_or_404
from .models import Movie, Review, RootReview, Article
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import MovieSerializer, ReviewSerializer, ArticleSerializer, RootSerializer, UserSerializers
from django.contrib.auth import get_user_model

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def index(request):
    movies = Movie.objects.all()
    serializers = MovieSerializer(movies, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializers = MovieSerializer(movie)
    return Response(serializers.data)

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

@api_view(['POST'])
@permission_classes([AllowAny])
def article(request):
    serializers = ArticleSerializer(data=request.data)
    if serializers.is_valid(raise_exception=True):
        serializers.save()
        return Response(serializers.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([AllowAny])
def update_delete(request, review_pk):
    review = get_object_or_404(RootReview, pk=review_pk)
    if request.method == 'PUT':
        serializer = RootReview(data=request.data, instance=review)
        if serializer.is_valid(reaise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        review.delete()
        return Response({'status': 204, 'message': '삭제되었습니다.'})

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
# @permission_classes([IsAuthenticated])
def user_detail(request, id):
    User = get_user_model()
    user = get_object_or_404(User, pk=id)
    serializers = UserSerializers(user)
    return Response(serializers.data)
