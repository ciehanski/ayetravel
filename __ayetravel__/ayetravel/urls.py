from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import app
from app import views

admin.autodiscover()
handler404 = app.views.handler404
handler500 = app.views.handler500

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('app.urls', namespace='app'), name='app'),
    path('accounts/', include('accounts.urls', namespace='accounts'), name='accounts'),
    path('my/trips/', include('trips.urls', namespace='trips'), name='trips'),
    path('community/', include('community.urls', namespace='community'), name='community'),
]
