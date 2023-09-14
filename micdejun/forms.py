from django import forms
from django.forms import TextInput, Textarea

from micdejun.models import Micdejun


class MicdejunForm(forms.ModelForm):
    class Meta:
        model = Micdejun
        fields = ['name', 'image', 'ingredients', 'small_description', 'mod_preparare']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter recipe name'}),
            'ingredients': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter recipe ingredients'}),
            'small_description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter small description'}),
            'mod_preparare': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter the steps'}),
        }
