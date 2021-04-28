from django.urls import path
from books import views as book_views

app_name = "books"

urlpatterns = [
    path("", book_views.HomeView.as_view(), name="books"),
    path("<int:pk>", book_views.BookDetail.as_view(), name="book_detail"),
    path("<int:pk>/edit/", book_views.EditBookView.as_view(), name="book_edit"),
    path("create/", book_views.CreateBookView.as_view(), name="book_create"),
]