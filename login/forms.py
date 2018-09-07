from django import forms
from django.core import validators


class UsernameTextBox(forms.Form):
    email = forms.CharField(max_length=50, required=True, label='',
                            widget=forms.TextInput(
                                attrs={'class': 'form-control',
                                       'placeholder': 'Username',
                                       'id': 'username_textbox',
                                       'type': 'text',
                                       'required': '',
                                       'name': 'username',
                                       }))

    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])


class PasswordTextBox(forms.Form):
    password = forms.CharField(max_length=60, required=True, label='',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control',
                                          'placeholder': 'Password',
                                          'id': 'password_textbox',
                                          'type': 'password',
                                          'required': '',
                                          'name': 'password',
                                          }))
