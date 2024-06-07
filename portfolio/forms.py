from django import forms # type: ignore
from .models import Portfo

class PortfoForm(forms.ModelForm):
    class Meta:
        model = Portfo
        fields = ['name', 'surname', 'age', 'city', 'university', 'hobby', 'skills']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'university': forms.TextInput(attrs={'class': 'form-control'}),
            'hobby': forms.Textarea(attrs={'class': 'form-control'}),
            'skills': forms.Textarea(attrs={'class': 'form-control'}),
        }
