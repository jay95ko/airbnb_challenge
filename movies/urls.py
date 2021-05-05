from django.urls import path
from . import views as movie_views

app_name = "movies"

urlpatterns = [
    path("", movie_views.HomeView.as_view(), name="movies"),
    path("<int:pk>", movie_views.MovieDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", movie_views.EditMovieView.as_view(), name="edit"),
    path("create/", movie_views.CreateMovieView.as_view(), name="create"),
]