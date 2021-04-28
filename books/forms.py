from django import forms
from . import models


class EditBookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = (
            "title",
            "year",
            "category",
            "rating",
            "writer",
            "cover_image",
        )

    def save(self, pk, *args, **kwargs):
        book = super().save(commit=False)
        book_pk = models.Book.objects.get(pk=pk)
        photo.save()