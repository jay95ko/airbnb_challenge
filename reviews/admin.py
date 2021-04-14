from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "text",
        "rating",
    )

    list_filter = (
        "text",
        "rating",
    )
