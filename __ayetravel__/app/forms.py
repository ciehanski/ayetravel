from django import forms
from app.models import Trips


class CreateTripForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    user_location = forms.CharField(max_length=100)
    destination = forms.CharField(max_length=100)
    start_date = forms.DateField()
    end_date = forms.DateField()
    budget = forms.IntegerField()
    participants = forms.IntegerField()
    picture = forms.ImageField()

    class Meta:
        model = Trips
        exclude = ['owner']
