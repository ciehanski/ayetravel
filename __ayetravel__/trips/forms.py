from django import forms
from trips.models import Trips


class CreateTripForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
                            attrs={'class': 'form-control',
                                   'type': 'text',
                                   'data-toggle': 'input-mask'}))

    budget = forms.IntegerField(widget=forms.NumberInput(
                                attrs={'class': 'form-control',
                                       'type': 'text',
                                       'data-toggle': 'input-mask'}))

    user_location = forms.CharField(widget=forms.TextInput(
                                     attrs={'class': 'form-control',
                                            'type': 'text',
                                            'data-toggle': 'input-mask'}))

    destination = forms.CharField(widget=forms.TextInput(
                                   attrs={'class': 'form-control',
                                          'type': 'text',
                                          'data-toggle': 'input-mask'}))

    start_date = forms.DateField(widget=forms.DateInput(
                                  attrs={'type': 'text',
                                         'class': 'form-control date',
                                         'id': 'singledaterange',
                                         'data-toggle': 'date-picker',
                                         'data-cancel-class': 'btn-warning'}))

    end_date = forms.DateField(widget=forms.DateInput(
                                attrs={'type': 'text',
                                       'class': 'form-control date',
                                       'id': 'singledaterange',
                                       'data-toggle': 'date-picker',
                                       'data-cancel-class': 'btn-warning'}))

    packing_list = forms.Textarea(attrs={'data-toggle': 'maxlength',
                                         'class': 'form-control',
                                         'maxlength': '2000',
                                         'rows': '10',
                                         'placeholder': 'Shampoo, soap, condoms, wine...'})

    public = forms.BooleanField(widget=forms.CheckboxInput(
                                  attrs={'type': 'checkbox',
                                         'id': 'switch3',
                                         'checked data-switch': 'success'}))

    class Meta:
        model = Trips
        fields = ['name', 'budget', 'user_location', 'destination', 'start_date',
                  'end_date', 'packing_list', 'public', 'files', 'picture']
