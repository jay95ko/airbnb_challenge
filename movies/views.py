from math import ceil
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from . import models


def movies(request):
    page = request.GET.get("page", 1)
    movie_list = models.Movie.objects.all()
    paginator = Paginator(movie_list, 10, orphans=5)
    try:
        movies = paginator.page(int(page))
        return render(request, "movies/movie.html", {"movies": movies})
    except:
        return redirect("/")


# Create your views here.
