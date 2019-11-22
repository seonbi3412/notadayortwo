from django.shortcuts import render, get_object_or_404
from .models import Movie, Review

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializer
# Create your views here.
@api_view(['GET'])
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
def review(request, movie_pk):
    return