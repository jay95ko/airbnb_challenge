from django.views.generic import DetailView
from django.shortcuts import render
from . import models


def categories(request):
    return render(request, "categories/category.html")


class CategoryDetail(DetailView):

    model = models.Category


# Create your views here.
