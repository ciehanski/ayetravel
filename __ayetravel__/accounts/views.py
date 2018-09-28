from django.shortcuts import render, get_object_or_404
from accounts.forms import LoginForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
import urllib
from urllib.request import urlopen
import json
from django.views.generic import TemplateView, FormView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import InsensitiveUser
from app.views import BaseViewMixin, get_notifications, get_user_trips, get_total_user_notifs, get_total_user_trips, \
    get_participants


class LoginView(FormView):
    context_object_name = 'login'
    template_name = 'accounts/login.html'
    login_form = LoginForm()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('app:index'))
        else:
            return render(request, self.template_name, {'form': self.login_form})

    def post(self, request, *args, **kwargs):
        username_form = request.POST.get('username_textbox')
        password_form = request.POST.get('password_textbox')
        remember_me_form = request.POST.get('remember_me_checkbox')
        botcatcher_form = request.POST.get('botcatcher')

        # Begin reCAPTCHA validation
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
        # End reCAPTCHA validation

        user = authenticate(username=username_form, password=password_form)

        if result['success'] and botcatcher_form is None:
            if user.is_active:
                if user:
                    # Log the user in
                    login(request, user)
                    # Handle remember me, don't expire user auth if checked
                    if not request.POST.get(remember_me_form, None):
                        # if checked, don't expire
                        request.session.set_expiry(0)
                    # return the redirect of index regardless of remember me checkbox outcome
                    return HttpResponseRedirect(reverse('app:index'))
                else:
                    # Account not active
                    return render(request, self.template_name, {'form': self.login_form,
                                                                'error': 'That password was incorrect. '
                                                                         'Please try again.'})
            else:
                # Password incorrect
                return render(request, self.template_name, {'form': self.login_form,
                                                            'error': 'That account is disabled.'})
        else:
            # recaptcha not completed or botcatcher textbox filled out - we have a bot
            return render(request, self.template_name, {'form': self.login_form,
                                                        'error': 'Please complete the reCAPTCHA verification form.'})


class LogoutView(LoginRequiredMixin, TemplateView):
    context_object_name = 'logout'
    template_name = 'accounts/logout.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, self.template_name)


class ProfileView(BaseViewMixin, DetailView):
    context_object_name = 'profile'
    template_name = 'accounts/profile.html'
    object = InsensitiveUser

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.cleaned_user_object(request)
        context['notifications'] = get_notifications(request)
        context['user_trips'] = get_user_trips(request)
        context['notif_total'] = get_total_user_notifs(request)
        context['total_user_trips'] = get_total_user_trips(request)
        context['participants'] = get_participants(request)
        return render(request, self.template_name, context)

    def get_object(self, queryset=InsensitiveUser):
        username_ = self.kwargs.get('username')
        return get_object_or_404(InsensitiveUser, username=username_)

    def cleaned_user_object(self, request):
        username_ = self.kwargs.get('username')
        obj = self.get_object()
        if obj.get_username() == request.user.get_username():
            return get_object_or_404(InsensitiveUser, username=username_)
        else:
            return render(request, 'app/base.html', {'error': 'This is a private account which you '
                                                              'do not have permissions to view.'})


class RecoveryView(LoginRequiredMixin, FormView):
    context_object_name = 'recovery'
    template_name = 'accounts/recovery.html'
    # form_class = ''

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


def get_current_user(request):
    return InsensitiveUser.objects.all().filter(username__iexact=request.user.get_username())
