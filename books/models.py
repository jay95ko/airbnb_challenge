from django.db import models
from core import models as core_models
from categories import models as category_models
from django.urls import reverse
from people import models as people_models


class Book(core_models.TimeStampedModel):
    title = models.CharField(max_length=50, null=True)
    year = models.DateField()
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="books"
    )
    cover_image = models.ImageField(upload_to="cover_img", null=True, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    writer = models.ForeignKey(people_models.Person, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("books:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title