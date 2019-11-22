from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=10)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_genres', blank=True)

class Actor(models.Model):
    name = models.CharField(max_length=20)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_actors', blank=True)

class Movie(models.Model):
    genres = models.ManyToManyField(Genre, related_name='movies')
    title = models.CharField(max_length=50)
    original_title = models.CharField(max_length=100)
    poster_url = models.TextField()
    description = models.TextField()
    score = models.FloatField()
    open_date = models.DateField()
    watchgrade = models.CharField(max_length=15, blank=True)
    actors = models.ManyToManyField(Actor, related_name='filmography', blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)


class Review(models.Model):
    content = models.CharField(max_length=150)
    score = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

