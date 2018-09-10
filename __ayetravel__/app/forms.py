from django import forms
from app.models import Trips


class CreateTripForm(forms.ModelForm):
    name = forms.CharField(max_length=50, blank=True)
    user_location = forms.CharField(max_length=100, blank=True)
    destination = forms.CharField(max_length=100, blank=True)
    start_date = forms.DateField()
    end_date = forms.DateField()
    budget = forms.IntegerField()
    participants = forms.IntegerField()
    picture = forms.ImageField(default='')

    class Meta:
        model = Trips
        exclude = 'owner'
