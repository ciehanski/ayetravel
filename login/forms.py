from django import forms
from django.core import validators


class LoginForm(forms.Form):
    username_textbox = forms.CharField(max_length=25, required=True, label='Username',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control',
                                          'placeholder': 'Enter your username',
                                          'id': 'username_textbox',
                                          'type': 'text',
                                          'name': 'username_textbox',
                                          }))

    botcatcher = forms.CharField(required=False, validators=[validators.MaxLengthValidator(0)],
                                 widget=forms.HiddenInput())

    password_textbox = forms.CharField(max_length=60, required=True, label='Password',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control',
                                          'placeholder': 'Enter your password',
                                          'id': 'password_textbox',
                                          'type': 'password',
                                          'name': 'password_textbox',
                                          }))

    remember_me_checkbox = forms.BooleanField(label='', required=False,
                                     widget=forms.CheckboxInput(
                                         attrs={'class': 'custom-control-input',
                                                'type': 'checkbox',
                                                'id': 'checkbox-signin',
                                                'name': 'remember_me_checkbox'
                                                }))
