from django.contrib.auth.models import AbstractUser
from django.db import models


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
    favourite_book_genre = models.CharField(max_length=15, null=True)
    favourite_movie_genre = models.CharField(max_length=15, null=True)