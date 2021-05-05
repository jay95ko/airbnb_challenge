from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.urls import reverse
from django.shortcuts import redirect
from . import models


class HomeView(ListView):
    model = models.Person
    paginate_by = 12
    paginate_orphans = 5
    context_object_name = "people"


class PersonDetail(DetailView):

    """ BookDetail Definition """

    model = models.Person


class EditPersonView(UpdateView):

    model = models.Person
    template_name = "people/person_edit.html"
    fields = (
        "name",
        "kind",
        "photo",
    )


class CreatePersonView(CreateView):

    model = models.Person
    template_name = "people/person_create.html"
    fields = (
        "name",
        "kind",
        "photo",
    )


"""
    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return redirect(reverse("people:person_detail", kwargs={"pk": self.object.pk}))


    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return super(CreatePersonView, self).form_valid(form)
        """