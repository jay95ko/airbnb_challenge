from django.contrib import admin
from . import models


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "year",
        "cover_image",
        "rating",
    )

    list_filter = (
        "title",
        "year",
        "cover_image",
        "rating",
    )
