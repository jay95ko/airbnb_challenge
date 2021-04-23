from django.views.generic import ListView
from . import models


class HomeView(ListView):
    model = models.Person
    paginate_by = 10
    paginate_orphans = 5
    context_object_name = "people"
