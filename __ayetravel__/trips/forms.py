from django import forms
from trips.models import Trips


class CreateTripForm(forms.ModelForm):
    class Meta:
        model = Trips
        fields = ('name', 'budget', 'user_location', 'destination', 'start_date',
                  'end_date', 'packing_list', 'public', 'files')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'type': 'text',
                                           'data-toggle': 'input-mask',
                                           'placeholder': 'Name'}),
            'budget': forms.NumberInput(attrs={'class': 'form-control',
                                               'type': 'number',
                                               'data-toggle': 'input-mask',
                                               'placeholder': '0'}),
            'user_location': forms.TextInput(attrs={'class': 'form-control',
                                                    'type': 'text',
                                                    'data-toggle': 'input-mask',
                                                    'placeholder': 'Drop your pin'}),
            'destination': forms.TextInput(attrs={'class': 'form-control',
                                                  'type': 'text',
                                                  'data-toggle': 'input-mask',
                                                  'placeholder': 'Destination'}),
            'start_date': forms.DateInput(attrs={'type': 'date',
                                                 'class': 'form-control date',
                                                 'id': 'singledaterange',
                                                 'data-toggle': 'date-picker',
                                                 'data-cancel-class': 'btn-warning',
                                                 'name': 'start_date'}),
            'end_date': forms.DateInput(attrs={'type': 'date',
                                               'class': 'form-control date',
                                               'id': 'singledaterange',
                                               'data-toggle': 'date-picker',
                                               'data-cancel-class': 'btn-warning',
                                               'name': 'end_date'}),
            'participants': forms.NumberInput(attrs={'type': 'number',
                                                     'class': 'form-control',
                                                     'id': 'participants_total',
                                                     'placeholder': '1'}),
            'packing_list': forms.Textarea(attrs={'data-toggle': 'maxlength',
                                                  'class': 'form-control',
                                                  'maxlength': '2000',
                                                  'rows': '10',
                                                  'placeholder': 'Shampoo, soap, condoms, wine...'}),
            'public': forms.CheckboxInput(attrs={'type': 'checkbox',
                                                 'id': 'switch3',
                                                 'checked data-switch': 'success'}),
            'files': forms.FileInput(attrs={'name': 'file',
                                            'type': 'file',
                                            'multiple': ''}),
        }
