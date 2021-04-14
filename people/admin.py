from django.contrib import admin
from . import models


@admin.register(models.Preson)
class PersonAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "kind",
        "photo",
    )

    list_filter = (
        "name",
        "kind",
        "photo",
    )
