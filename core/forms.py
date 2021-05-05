from django import forms
from django_countries.fields import CountryField
from . import models


class SearchForm(forms.Form):

    category = forms.CharField(initial="category")
    select_component = [("book", "book"), ("movie", "movie"), ("person", "person")]
    select = forms.ChoiceField(choices=select_component)