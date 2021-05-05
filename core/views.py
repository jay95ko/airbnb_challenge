from django.views.generic import View, ListView
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from books import models as book_models
from movies import models as movie_models
from people import models as person_models
from categories import models as category_models

# Create your views here.
def home(request):
    person_page = request.GET.get("page1", 1)
    person_list = person_models.Person.objects.all().order_by("pk")
    paginator_person = Paginator(person_list, 10, orphans=2)
    try:
        people = paginator_person.page(int(person_page))
    except PageNotAnInteger:
        people = paginator_person.page(1)
    except EmptyPage:
        people = paginator_person.page(paginator_person.num_pages)
    except:
        return redirect("/")

    movie_page = request.GET.get("page2", 1)
    movie_list = movie_models.Movie.objects.all().order_by("pk")
    paginator_movie = Paginator(movie_list, 10, orphans=2)
    try:
        movies = paginator_movie.page(int(movie_page))
    except PageNotAnInteger:
        movies = paginator_movie.page(1)
    except EmptyPage:
        movies = paginator_movie.page(paginator_movie.num_pages)
    except:
        return redirect("/")

    book_page = request.GET.get("page3", 1)
    book_list = book_models.Book.objects.all().order_by("pk")
    paginator_book = Paginator(book_list, 10, orphans=2)
    try:
        books = paginator_book.page(int(book_page))
    except PageNotAnInteger:
        books = paginator_book.page(1)
    except EmptyPage:
        books = paginator_book.page(paginator_book.num_pages)
    except:
        return redirect("/")

    return render(
        request,
        "home/homes.html",
        {
            "person_page": person_page,
            "movie_page": movie_page,
            "book_page": book_page,
            "books": books,
            "movies": movies,
            "people": people,
        },
    )


class SearchView(ListView):
    model = category_models.Category
    paginate_by = 10
    paginate_orphans = 5
    context_object_name = "categories"