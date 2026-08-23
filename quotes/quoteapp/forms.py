from django import forms
from django.forms import ModelForm
from .models import Author, Quote

class AuthorForm(ModelForm):

    class Meta:

        model = Author

        fields = ['fullname', 'born_date', 'born_location', 'description']

        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

class QuoteForm(ModelForm):

    class Meta:

        model = Quote

        fields = ['quote', 'tags', 'author']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
            'author': forms.Select(attrs={'class': 'form-select'}),
            'quote': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }