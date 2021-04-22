from math import ceil
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from . import models


def books(request):
    page = request.GET.get("page", 1)
    book_list = models.Book.objects.all()
    paginator = Paginator(book_list, 10, orphans=5)
    try:
        books = paginator.page(int(page))
        print(books)
        return render(request, "books/book.html", {"books": books})
    except:
        return redirect("/")


# Create your views here.
