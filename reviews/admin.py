from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ("created_by", "movie", "book", "rating")

    list_filter = ("movie", "book")
