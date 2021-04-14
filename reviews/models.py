from django.db import models
from core import models as core_models
from users import models as user_models
from books import models as book_models
from movies import models as movie_models


class Review(core_models.TimeStampedModel):

    created_by = models.ForeignKey(
        user_models.User, on_delete=models.CASCADE, null=True
    )
    text = models.TextField()
    movie = models.ForeignKey(
        movie_models.Movie, on_delete=models.CASCADE, null=True, blank=True
    )
    book = models.ForeignKey(
        book_models.Book, on_delete=models.CASCADE, null=True, blank=True
    )
    rating = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name_plural = "People"
