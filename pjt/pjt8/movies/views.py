from django.shortcuts import render,get_list_or_404,redirect
from django.views.decorators.http import require_safe
from .models import Movie,Genre
import random


# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    genres= movie.genres.all()
    context = {
        'movie': movie,
        'genres': genres,
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    if request.user.is_authenticated:
        genres_set = list(set(Movie.objects.values_list('genres')))
        choices = random.choice(genres_set)
        movies = Movie.objects.filter(genres=choices[0]).order_by('-vote_average')[:10]
        genres = Genre.objects.get(pk=choices[0])
        context = {
            'movies': movies,
            'genres': genres,
        }
        return render(request, 'movies/recommended.html', context)
    return redirect('accounts:login')