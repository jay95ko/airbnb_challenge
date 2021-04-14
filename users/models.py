from django.contrib.auth.models import AbstractUser
from django.db import models
from categories import models as category_models


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    PREFERENCE_BOOK = "Books"
    PREFERENCE_MOVIES = "Movies"
    PREFERENCE_CHOICES = ((PREFERENCE_BOOK, "Books"), (PREFERENCE_MOVIES, "Movies"))

    LANGUAGE_KOREAN = "kr"
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_CHOICES = ((LANGUAGE_KOREAN, "Korean"), (LANGUAGE_ENGLISH, "English"))
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True)
    preference = models.CharField(choices=PREFERENCE_CHOICES, max_length=10, null=True)
    bio = models.TextField(default="")
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, null=True)
    favourite_book_genre = models.ForeignKey(
        category_models.Category,
        on_delete=models.CASCADE,
        null=True,
        related_name="fav_book_genre",
    )
    favourite_movie_genre = models.ForeignKey(
        category_models.Category,
        on_delete=models.CASCADE,
        null=True,
        related_name="fav_movie_genre",
    )

    def __str__(self):
        return self.username