from math import ceil
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from . import models


def people(request):
    page = request.GET.get("page", 1)
    person_list = models.Person.objects.all()
    paginator = Paginator(person_list, 10, orphans=5)
    try:
        people = paginator.page(int(page))
        return render(request, "people/person.html", {"people": people})
    except:
        return redirect("/")


# Create your views here.
