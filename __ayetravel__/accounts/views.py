from django.shortcuts import render
from accounts import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
import urllib
import json
from django.views.generic import TemplateView, FormView, DetailView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(FormView):
    context_object_name = 'accounts'
    template_name = 'accounts/login.html'
    login_form = forms.LoginForm()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('app:index'))
        else:
            return render(request, 'accounts/login.html', {'form': self.login_form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            username_form = request.POST.get('username_textbox')
            password_form = request.POST.get('password_textbox')
            remember_me_form = request.POST.get('remember_me_checkbox')
            botcatcher_form = request.POST.get('botcatcher')
            print(botcatcher_form)
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

            if result['success'] and botcatcher_form is None:
                if user:
                    if user.is_active:
                        login(request, user)
                        # Handle remember me, don't expire user auth
                        if not request.POST.get(remember_me_form, None):
                            request.session.set_expiry(0)
                        return HttpResponseRedirect(reverse('app:index'))
                    else:
                        # Account not active
                        return render(request, 'accounts/login.html', {'form': self.login_form,
                                                                       'error': 'Account not active.'})
                else:
                    # Not a valid user
                    return render(request, 'accounts/login.html', {'form': self.login_form,
                                                                   'error': 'Not a valid user.'})
            else:
                # recaptcha not completed or botcatcher textbox filled out - we have a bot
                return render(request, 'accounts/login.html', {'form': self.login_form,
                                                               'error': 'Please complete recaptcha.'})
        else:
            # Empty response
            return render(request, 'accounts/login.html', {'form': self.login_form,
                                                           'error': 'Empty response, please refresh your browser.'})


class LogoutView(LoginRequiredMixin, RedirectView):
    context_object_name = 'logout'
    template_name = 'accounts/logout.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'accounts/logout.html')


class ProfileView(LoginRequiredMixin, DetailView):
    context_object_name = 'profile'
    template_name = 'accounts/profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/profile.html')


class RecoveryView(LoginRequiredMixin, FormView):
    context_object_name = 'recovery'
    template_name = 'accounts/recovery.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/recovery.html')
