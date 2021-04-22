from django.urls import path
from books import views as book_views

app_name = "book"

urlpatterns = [
    path("", book_views.books, name="books"),
]