from django import forms
from .models import City


class CityForm(forms.ModelForm):
    name = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'City name'}))

    class Meta:
        model = City
        fields = ("name", )
