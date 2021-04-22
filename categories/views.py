from math import ceil
from django.shortcuts import render
from . import models


def categories(request):
    return render(request, "categories/category.html")


# Create your views here.
