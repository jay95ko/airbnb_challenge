from django.urls import path
from . import views as core_views


app_name = "core"

urlpatterns = [
    path("", core_views.home, name="home"),
    path("search/", core_views.SearchView.as_view(), name="search"),
]