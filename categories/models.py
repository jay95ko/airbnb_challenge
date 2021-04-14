from django.db import models
from core import models as core_models


class Category(core_models.TimeStampedModel):

    KIND_BOOK = "book"
    KIND_MOVIE = "movie"
    KIND_BOTH = "both"
    KIND_CHOICES = (
        (KIND_BOOK, "Book"),
        (KIND_MOVIE, "Movie"),
        (KIND_BOTH, "Both"),
    )

    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=5, choices=KIND_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"