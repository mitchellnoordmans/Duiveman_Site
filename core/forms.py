# forms.py

from django import forms
from .models import Offerte, Service

from django import forms

class OfferteForm(forms.ModelForm):
    

    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Offerte
        fields = ['name', 'email', 'adres', 'postcode', 'woonplaats', 'telefoon_nummer', 'services', 'uw_aanvraag']
