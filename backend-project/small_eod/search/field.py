from django.db.models import Q
from django import forms
from .grammar import parse

class SearchField(forms.CharField):
    def clean(self, *args, **kwargs):
        value = super().clean(*args, **kwargs)
        return parse(value)