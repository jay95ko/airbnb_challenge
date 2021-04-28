from django.urls import path
from . import views as movie_views

app_name = "movies"

urlpatterns = [
    path("", movie_views.HomeView.as_view(), name="movies"),
    path("<int:pk>", movie_views.MovieDetail.as_view(), name="movie_detail"),
    path("<int:pk>/edit/", movie_views.EditMovieView.as_view(), name="movie_edit"),
    path("create/", movie_views.CreateMovieView.as_view(), name="movie_create"),
]