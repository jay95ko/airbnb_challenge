from django.db import models
from core import models as core_models
from categories import models as category_models
from people import models as people_models


class Book(core_models.TimeStampedModel):
    title = models.CharField(max_length=50, null=True)
    year = models.DateField()
    category = models.ManyToManyField(category_models.Category, blank=True)
    cover_image = models.ImageField(null=True, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    writer = models.ForeignKey(people_models.Preson, on_delete=models.CASCADE)

    def __str__(self):
        return self.title