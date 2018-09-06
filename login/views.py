from django.shortcuts import render
from login import forms
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, '../templates/registration/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def login_view(request):
    username_textbox = forms.UsernameTextBox()
    password_textbox = forms.PasswordTextBox()

    if request.method == 'POST':
        username_form = request.POST.get('username')
        password_form = request.POST.get('password')
        user = authenticate(username=username_form, password=password_form)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, '../templates/registration/login.html', HttpResponse('Account Not Active'))
        else:
            return render(request, '../templates/registration/login.html', HttpResponse('Invalid Login Details Supplied'))
    else:
        return render(request, '../templates/registration/login.html', {'email_textbox': username_textbox,
                                                                        'password_textbox': password_textbox})
