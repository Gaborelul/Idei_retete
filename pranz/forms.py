from django import forms
from django.forms import TextInput, Textarea

from pranz.models import Pranz


class PranzForm(forms.ModelForm):

    class Meta:
        model = Pranz
        fields = ['name', 'image', 'ingredients', 'description']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter recipe name'}),
            'ingredients': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter recipe ingredients'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter recipe description'}),
        }
