# forms.py

from django import forms
from .models import Offerte

class OfferteForm(forms.ModelForm):
    class Meta:
        model = Offerte
        fields = ['name', 'email', 'adres', 'postcode', 'woonplaats', 'telefoon_nummer', 'services', 'uw_aanvraag']
