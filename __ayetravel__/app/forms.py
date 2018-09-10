from django import forms
from app.models import Trips


class CreateTripForm(forms.ModelForm):
    class Meta:
        model = Trips
        fields = '__all__'
