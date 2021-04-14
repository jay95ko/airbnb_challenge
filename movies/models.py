from django.db import models
from core import models as core_models
from categories import models as category_models
from people import models as people_models


class Movie(core_models.TimeStampedModel):
    title = models.CharField(max_length=50)
    year = models.DateField()
    cover_image = models.ImageField(null=True, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField(category_models.Category, blank=True)
    director = models.ForeignKey(
        people_models.Preson,
        on_delete=models.CASCADE,
        null=True,
        related_name="Derector",
    )
    cast = models.ManyToManyField(
        people_models.Preson, related_name="Actors", blank=True
    )

    def __str__(self):
        return self.title