from django.urls import path
from . import views as people_views

app_name = "people"

urlpatterns = [
    path("", people_views.people, name="people"),
]