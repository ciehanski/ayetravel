from django.shortcuts import render
from login import forms
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
import urllib
import json
from django.views.generic import TemplateView


class LoginView(TemplateView):
    context_object_name = 'login'
    template_name = 'registration/login.html'
    login_render = ''

    def get(self, request, *args, **kwargs):
        username_textbox = forms.UsernameTextBox()
        password_textbox = forms.PasswordTextBox()
        global login_render
        login_render = render(request, 'registration/login.html', {'email_textbox': username_textbox,
                                                                   'password_textbox': password_textbox})
        return login_render

    def post(self, request, *args, **kwargs):
        global login_render
        if request.method == 'POST':
            username_form = request.POST.get('username')
            password_form = request.POST.get('password')
            user = authenticate(username=username_form, password=password_form)
            if user is not None:

                ''' Begin reCAPTCHA validation '''
                recaptcha_response = request.POST.get('g-recaptcha-response')
                url = 'https://www.google.com/recaptcha/api/siteverify'
                values = {
                    'secret': '6Lcxam4UAAAAAMJYHMLc6obuBA6R1DHYHHfavqph',
                    'response': recaptcha_response
                }
                data = urllib.parse.urlencode(values).encode()
                req = urllib.request.Request(url, data=data)
                response = urllib.request.urlopen(req)
                result = json.loads(response.read().decode())
                ''' End reCAPTCHA validation '''
                # Check reCAPTCHA verification
                if result['success']:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect(reverse('index'))
                    else:
                        # Account not active
                        print('Account not active')
                        return login_render
                else:
                    # recaptcha not completed
                    print('reCAPTCHA not completed')
                    return login_render
            else:
                # Not a valid user
                print(f'Not a valid user: {username_form} {password_form}')
                return login_render
        else:
            return login_render


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
