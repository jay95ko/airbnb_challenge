from django.db import models
from core import models as core_models
from django.urls import reverse
from categories import models as category_models
from people import models as people_models


class Movie(core_models.TimeStampedModel):
    title = models.CharField(max_length=50)
    year = models.DateField()
    cover_image = models.ImageField(blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="movies"
    )
    director = models.ForeignKey(
        people_models.Person,
        on_delete=models.CASCADE,
        null=True,
        related_name="Derector",
    )
    cast = models.ManyToManyField(
        people_models.Person, related_name="Actors", blank=True
    )

    def get_absolute_url(self):
        return reverse("movies:movie_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title