from django.shortcuts import render
from .models import Movie, Review

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)