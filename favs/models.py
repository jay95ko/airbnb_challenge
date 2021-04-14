from django.db import models
from core import models as core_models
from users import models as user_models
from books import models as book_models
from movies import models as movie_models


class FavList(core_models.TimeStampedModel):

    created_by = models.OneToOneField(
        user_models.User, on_delete=models.CASCADE, primary_key=True
    )
    books = models.ManyToManyField(book_models.Book, blank=True)
    movies = models.ManyToManyField(movie_models.Movie, blank=True)

    class Meta:
        verbose_name = "Favorite List"
