from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model =Book
        fields=['title','author','description','isbn','published_date','cover_photo','file']
        widgets={
            'published_date':forms.DateInput(attrs={'type':'date'}),
        }