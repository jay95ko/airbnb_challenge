from django.contrib import admin
from . import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):

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