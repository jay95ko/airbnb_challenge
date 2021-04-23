from django.urls import path
from . import views as movie_views

app_name = "movie"

urlpatterns = [
    path("", movie_views.HomeView.as_view(), name="movie"),
]