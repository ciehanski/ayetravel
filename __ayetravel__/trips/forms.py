from django import forms
from trips.models import Trips


class CreateTripForm(forms.ModelForm):
    class Meta:
        model = Trips
        fields = ['name', 'budget', 'user_location', 'destination', 'start_date',
                  'end_date', 'packing_list', 'public', 'files', 'picture']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'type': 'text',
                                           'data-toggle': 'input-mask'}),
            'budget': forms.NumberInput(attrs={'class': 'form-control',
                                               'type': 'text',
                                               'data-toggle': 'input-mask'}),
            'user_location': forms.TextInput(attrs={'class': 'form-control',
                                                    'type': 'text',
                                                    'data-toggle': 'input-mask'}),
            'destination': forms.TextInput(attrs={'class': 'form-control',
                                                  'type': 'text',
                                                  'data-toggle': 'input-mask'}),
            'start_date': forms.DateInput(attrs={'type': 'text',
                                                 'class': 'form-control date',
                                                 'id': 'singledaterange',
                                                 'data-toggle': 'date-picker',
                                                 'data-cancel-class': 'btn-warning'}),
            'end_date': forms.DateInput(attrs={'type': 'text',
                                               'class': 'form-control date',
                                               'id': 'singledaterange',
                                               'data-toggle': 'date-picker',
                                               'data-cancel-class': 'btn-warning'}),
            'packing_list': forms.Textarea(attrs={'data-toggle': 'maxlength',
                                                  'class': 'form-control',
                                                  'maxlength': '2000',
                                                  'rows': '10',
                                                  'placeholder': 'Shampoo, soap, condoms, wine...'}),
            'public': forms.CheckboxInput(attrs={'type': 'checkbox',
                                                 'id': 'switch3',
                                                 'checked data-switch': 'success'}),
            'files': forms.FileInput(),
            'picture': forms.FileInput(),
        }
