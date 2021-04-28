from django.urls import path
from . import views as people_views

app_name = "people"

urlpatterns = [
    path("", people_views.HomeView.as_view(), name="people"),
    path("<int:pk>", people_views.PersonDetail.as_view(), name="person_detail"),
    path("<int:pk>/edit/", people_views.EditPersonView.as_view(), name="person_edit"),
    path("create/", people_views.CreatePersonView.as_view(), name="person_create"),
]