from django.shortcuts import render
from login import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
import urllib
import json
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(FormView):
    context_object_name = 'login'
    template_name = '../../login/templates/login/login.html'
    login_form = forms.LoginForm()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('app:index'))
        else:
            return render(request, '../../login/templates/login/login.html', {'form': self.login_form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            username_form = request.POST.get('username_textbox')
            password_form = request.POST.get('password_textbox')
            remember_me_form = request.POST.get('remember_me_checkbox')
            user = authenticate(username=username_form, password=password_form)

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

            if result['success']:
                if user:
                    if user.is_active:
                        login(request, user)
                        # Handle remember me, don't expire user auth
                        if not request.POST.get(remember_me_form, None):
                            request.session.set_expiry(0)
                        return HttpResponseRedirect(reverse('app:index'))
                    else:
                        # Account not active
                        return render(request, '../../login/templates/login/login.html', {'form': self.login_form})
                else:
                    # Not a valid user
                    return render(request, '../../login/templates/login/login.html', {'form': self.login_form})
            else:
                # recaptcha not completed
                return render(request, '../../login/templates/login/login.html', {'form': self.login_form})
        else:
            # Empty response
            return render(request, '../../login/templates/login/login.html', {'form': self.login_form})


class LogoutView(LoginRequiredMixin, TemplateView):
    context_object_name = 'logout'
    template_name = '../../login/templates/login/logout.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, '../../login/templates/login/logout.html')


class ProfileView(LoginRequiredMixin, TemplateView):
    context_object_name = 'profile'
    template_name = '../../login/templates/login/profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, '../../login/templates/login/profile.html')


class RecoveryView(LoginRequiredMixin, TemplateView):
    context_object_name = 'recovery'
    template_name = '../../login/templates/login/recovery.html'

    def get(self, request, *args, **kwargs):
        return render(request, '../../login/templates/login/recovery.html')

