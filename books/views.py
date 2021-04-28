from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from . import models


class HomeView(ListView):
    model = models.Book
    paginate_by = 10
    paginate_orphans = 5
    context_object_name = "books"


class BookDetail(DetailView):

    """ BookDetail Definition """

    model = models.Book


class EditBookView(UpdateView):

    model = models.Book
    template_name = "books/book_edit.html"
    fields = (
        "title",
        "year",
        "category",
        "rating",
        "writer",
        "cover_image",
    )


class CreateBookView(CreateView):

    model = models.Book
    template_name = "books/book_create.html"
    fields = (
        "title",
        "year",
        "category",
        "rating",
        "writer",
        "cover_image",
    )
