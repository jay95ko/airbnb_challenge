from django.urls import path
from . import views as category_views

app_name = "category"

urlpatterns = [
    path("", category_views.categories, name="category"),
    path("<int:pk>/", category_views.CategoryDetail.as_view(), name="detail"),
]