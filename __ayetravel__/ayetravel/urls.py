"""ayetravel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import app
from app import views

handler404 = app.views.handler404
handler500 = app.views.handler500

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('app.urls', namespace='app'), name='app'),
    path('accounts/', include('accounts.urls', namespace='accounts'), name='accounts'),
    path('my/trips/', include('trips.urls', namespace='trips'), name='trips'),
    # path('community/', include('community.urls', namespace='community'), name='community'),
]
