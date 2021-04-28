from django.db import models
from django.urls import reverse
from core import models as core_models


class Person(core_models.TimeStampedModel):

    KIND_ACTOR = "actor"
    KIND_DIRECTOR = "director"
    KIND_WRITER = "writer"
    KIND_CHOICES = (
        (KIND_ACTOR, "Actor"),
        (KIND_DIRECTOR, "Director"),
        (KIND_WRITER, "Writer"),
    )

    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=8, choices=KIND_CHOICES)
    photo = models.ImageField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("people:person_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name