from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.urls import reverse
from django.shortcuts import redirect
from . import models


class HomeView(ListView):
    model = models.Movie
    paginate_by = 10
    paginate_orphans = 5
    context_object_name = "movies"


class MovieDetail(DetailView):

    """ BookDetail Definition """

    model = models.Movie


class EditMovieView(UpdateView):

    model = models.Movie
    template_name = "movies/movie_edit.html"
    fields = (
        "title",
        "year",
        "rating",
        "category",
        "director",
        "cast",
        "cover_image",
    )


class CreateMovieView(CreateView):

    model = models.Movie
    template_name = "movies/movie_create.html"
    fields = (
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "director",
        "cast",
    )
